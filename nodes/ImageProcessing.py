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

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import String
font = cv2.FONT_HERSHEY_COMPLEX

rospy.init_node('imageprogressing', anonymous=True)
pub = rospy.Publisher("/camera/image/coordinates", Int16MultiArray, queue_size=10)
l_h = 0
l_s = 0
l_v = 0
u_h = 0
u_s = 0
u_v = 0

def callback(data):

    np_arr = np.fromstring(data.data, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    filterd = cv2.inRange(hsv, (l_h, l_s, l_v), (u_h, u_s, u_v))
    _, contours, _ = cv2.findContours(filterd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Anzahl = 0

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4 and cv2.contourArea(cnt) >= 100 and cv2.contourArea(cnt) <= 1000000:
            xmittelpunkt = (approx.ravel()[0] + approx.ravel()[2] + approx.ravel()[4] + approx.ravel()[6]) / 4
            ymittelpunkt = (approx.ravel()[1] + approx.ravel()[3] + approx.ravel()[5] + approx.ravel()[7]) / 4
            dabei = False
            #            checke ob das Viereck schon erkannt wurde
            list = []
            for elm in list:
                if (xmittelpunkt - elm[0] <= 1 or xmittelpunkt - elm[0] >= 1 or ymittelpunkt - elm[
                    1] <= 1 or ymittelpunkt - elm[1] >= 1):
                    dabei = True
            if dabei == False:
                Anzahl = Anzahl + 1
                drehung = np.arctan(
                    (approx.ravel()[3] - approx.ravel()[1]) / (approx.ravel()[2] - approx.ravel()[0]))
                drehung = drehung / np.pi * 180
                cv2.drawContours(image, [approx], 0, (0), 5)
                list =[xmittelpunkt, ymittelpunkt, int(drehung)]
                if not xmittelpunkt < 480:
                    xmittelpunkt = 479;
                if not ymittelpunkt < 480:
                    ymittelpunkt = 479;
                color = image[int(xmittelpunkt), int(ymittelpunkt)]
                cv2.putText(image, "B:" + str(color[0]) + " G:" + str(color[1]) + " R:" + str(color[2]),
                            (int(xmittelpunkt), int(ymittelpunkt)), font, 1, (0))
            publish(list)
    cv2.imshow('frame', image)
    cv2.imshow('filterd', filterd)
    cv2.waitKey(10)

def changeValues(data):
    val = data.data.split(":")

    if val[0] == "l_h":
        global l_h
        l_h = int(val[1])

    elif val[0] == "l_s":
        global l_s
        l_s = int(val[1])

    elif val[0] == "l_v":
        global l_v
        l_v = int(val[1])

    elif val[0] == "u_h":
        global u_h
        u_h = int(val[1])

    elif val[0] == "u_s":
        global u_s
        u_s = int(val[1])

    elif val[0] == "u_v":
        global u_v
        u_v = int(val[1])

    rospy.loginfo("New Filter Settings: %d; %d; %d;_______%d; %d; %d;" %(l_h, l_s, l_v, u_h, u_s, u_v))


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.Subscriber('/camera/image/compressed', CompressedImage, callback)
    rospy.Subscriber("/camera/settings", String, changeValues)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def publish(list):

    #rate = rospy.Rate(25) # 10hz
    msg = Int16MultiArray()
    msg.data = list
    # Publish new image
    pub.publish(msg)
        #rate.sleep()


if __name__ == '__main__':
    listener()

