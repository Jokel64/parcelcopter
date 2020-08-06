#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2020, Hannes Pfitzner, Jakob Englert, Joachim Hecker
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Receives images from CameraImagePub, processes and publishes coordinates
from __future__ import division

import rospy
import numpy as np
from math import atan
import cv2
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import CompressedImage


class ImgProcessor:
    def __init__(self):
        rospy.init_node('parcelposition', anonymous=True)
        rate = rospy.Rate(1)
        self.cam_pos_pub = rospy.Publisher("parcel/position", PoseStamped, queue_size=1)
        self.subscriber_image = rospy.Subscriber('/iris/usb_cam/image_raw/compressed', CompressedImage, self.callback,
                                                 queue_size=1)
        self.sub_camset = rospy.Subscriber("/camera/settings", String, self.changeValues)
        self.l_h = 0
        self.l_s = 0
        self.l_v = 0
        self.u_h = 179
        self.u_s = 255
        self.u_v = 255
        rospy.loginfo("Image Processing started.")
        self.last_request = rospy.get_rostime()
        self.listener()

    def callback(self, data):
        now = rospy.get_rostime()
        if ((now - self.last_request) > rospy.Duration(0.1)):
            self.last_request = now
            font = cv2.FONT_HERSHEY_COMPLEX
            np_arr = np.fromstring(data.data, np.uint8)
            image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            filterd = cv2.inRange(hsv, (self.l_h, self.l_s, self.l_v), (self.u_h, self.u_s, self.u_v))
            filterd = cv2.GaussianBlur(filterd, (5, 5), cv2.BORDER_DEFAULT)

            _, contours, _ = cv2.findContours(filterd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            print(contours)

            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
                print("new")
                print(approx)
                if len(approx) == 4:
                    xmittelpunkt = (approx.ravel()[0] + approx.ravel()[2] + approx.ravel()[4] + approx.ravel()[6]) / 4
                    ymittelpunkt = (approx.ravel()[1] + approx.ravel()[3] + approx.ravel()[5] + approx.ravel()[7]) / 4
                    dabei = False
                    #            checke ob das Viereck schon erkannt wurde
                    list = []
                    position = PoseStamped()
                    for elm in list:

                        if (xmittelpunkt - elm[0] <= 1 or xmittelpunkt - elm[0] >= 1 or ymittelpunkt - elm[
                            1] <= 1 or ymittelpunkt - elm[1] >= 1):
                            dabei = True
                    if dabei == False:
                        x = [approx.ravel()[0], approx.ravel()[1]]
                        for i in range(3):
                            if approx.ravel()[(i + 1) * 2 + 1] < x[1]:
                                x = [approx.ravel()[(i + 1) * 2], approx.ravel()[(i + 1) * 2 + 1]]

                        y = [500, 500]
                        for i in range(4):
                            if approx.ravel()[i * 2 + 1] < y[1]:
                                if not (x == [approx.ravel()[i * 2], approx.ravel()[i * 2 + 1]]):
                                    y = [approx.ravel()[i * 2], approx.ravel()[i * 2 + 1]]
                        print([x, y])
                        s = (x[1] - y[1]) / (x[0] - y[0])
                        print(s)
                        drehung = atan(s)
                        drehung = drehung / np.pi * 180
                        print(drehung)
                        position.pose.position.x = xmittelpunkt
                        position.pose.position.y = ymittelpunkt
                        position.pose.position.z = int(drehung)
                        cv2.drawContours(image, [approx], 0, 0, 5)
                        if not xmittelpunkt < 240:
                            xmittelpunkt = 239
                        if not ymittelpunkt < 240:
                            ymittelpunkt = 239
                        self.cam_pos_pub.publish(position)
                        # mitte des bilder bei 160, 104
                        color = image[int(xmittelpunkt), int(ymittelpunkt)]
                        cv2.putText(image, "B:" + str(color[0]) + " G:" + str(color[1]) + " R:" + str(color[2]),
                                    (int(xmittelpunkt), int(ymittelpunkt)), font, 1, (0))

            cv2.imshow('frame', image)
            cv2.imshow('filterd', filterd)
            cv2.waitKey(10)

    def changeValues(self, data):
        val = data.data.split(":")

        if val[0] == "l_h":
            self.l_h = int(val[1])

        elif val[0] == "l_s":
            self.l_s = int(val[1])

        elif val[0] == "l_v":
            self.l_v = int(val[1])

        elif val[0] == "u_h":
            self.u_h = int(val[1])

        elif val[0] == "u_s":
            self.u_s = int(val[1])

        elif val[0] == "u_v":
            self.u_v = int(val[1])

        rospy.loginfo("New Filter Settings: %d; %d; %d;_______%d; %d; %d;" % (
        self.l_h, self.l_s, self.l_v, self.u_h, self.u_s, self.u_v))

    def listener(self):

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()


if __name__ == '__main__':
    imgPc = ImgProcessor()
