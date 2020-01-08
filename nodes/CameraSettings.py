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

## Provides Settings for the image processing

import rospy
import cv2
from std_msgs.msg import String


def nothing(x):
    pass


def createMsg(type, value):
    return "%s:%d" % (type, value)


def talker():
    rospy.loginfo("Camera Settings started.")

    cv2.namedWindow("Trackbars")

    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

    cv2.createTrackbar("Min Size", "Trackbars", 0, 2000, nothing)
    cv2.createTrackbar("Max Size", "Trackbars", 2000, 2000, nothing)

    pub = rospy.Publisher("/camera/settings", String, queue_size=10)
    rospy.init_node("SettingsProvider", anonymous=True)
    #rate = rospy.Rate(50)  # 2hz
    l_h = 0
    l_s = 0
    l_v = 0
    u_h = 0
    u_s = 0
    u_v = 0
    l_size = 0
    u_size = 2000


    while not rospy.is_shutdown():
        if l_h != cv2.getTrackbarPos("L - H", "Trackbars"):
            l_h = cv2.getTrackbarPos("L - H", "Trackbars")
            pub.publish(createMsg("l_h", l_h))

        if l_s != cv2.getTrackbarPos("L - S", "Trackbars"):
            l_s = cv2.getTrackbarPos("L - S", "Trackbars")
            pub.publish(createMsg("l_s", l_s))

        if l_v != cv2.getTrackbarPos("L - V", "Trackbars"):
            l_v = cv2.getTrackbarPos("L - V", "Trackbars")
            pub.publish(createMsg("l_v", l_v))

        if u_h != cv2.getTrackbarPos("U - H", "Trackbars"):
            u_h = cv2.getTrackbarPos("U - H", "Trackbars")
            pub.publish(createMsg("u_h", u_h))

        if u_s != cv2.getTrackbarPos("U - S", "Trackbars"):
            u_s = cv2.getTrackbarPos("U - S", "Trackbars")
            pub.publish(createMsg("u_s", u_s))

        if u_v != cv2.getTrackbarPos("U - V", "Trackbars"):
            u_v = cv2.getTrackbarPos("U - V", "Trackbars")
            pub.publish(createMsg("u_v", u_v))

        if l_size != cv2.getTrackbarPos("Min Size", "Trackbars"):
            l_size = cv2.getTrackbarPos("Min Size", "Trackbars")
            pub.publish(createMsg("l_size", l_size))

        if u_size != cv2.getTrackbarPos("Max Size", "Trackbars"):
            u_size = cv2.getTrackbarPos("Max Size", "Trackbars")
            pub.publish(createMsg("u_size", u_size))

        cv2.waitKey(100)
        #rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
