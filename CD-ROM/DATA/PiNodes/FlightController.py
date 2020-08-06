#!/usr/bin/env python

import numpy as np
import rospy
import mavros
from math import cos, sin, fabs, sqrt, radians
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Quaternion
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode
from tf.transformations import quaternion_from_euler, euler_from_quaternion


# callback method for state sub
class FlightController:
    def __init__(self):
        rospy.init_node('position', anonymous=True)
        rate = rospy.Rate(20.0)
        self.state = State()
        offb_set_mode = SetMode
        self.local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=1)
        arming_client = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)
        set_mode_client = rospy.ServiceProxy('mavros/set_mode', SetMode)
        state_sub = rospy.Subscriber('mavros/state', State, self.state_cb)
        while not self.state.connected:
            rate.sleep()
        rospy.loginfo("Connected")
        prev_state = self.state
        last_request = rospy.get_rostime()
        self.target = PoseStamped()
        self.target.pose.position.x = 0
        self.target.pose.position.y = 0
        self.target.pose.position.z = 0
        self.winkelbeschleunigung = 1000
        rospy.loginfo(
            "I AM HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        while not (self.state.armed and self.state.mode == "OFFBOARD"):
            self.local_pos_pub.publish(self.target)
            now = rospy.get_rostime()
            if self.state.mode != "OFFBOARD" and (now - last_request > rospy.Duration(5.)):
                rospy.loginfo("Try to put Mode to Offborad")
                set_mode_client(base_mode=0, custom_mode="OFFBOARD")
                last_request = now
            else:
                if not self.state.armed and (now - last_request > rospy.Duration(5.)):
                    rospy.loginfo("Try to arm vehicle")
                    arming_client(True)
                    last_request = now
            if prev_state.armed != self.state.armed:
                rospy.loginfo("Vehicle armed: %r" % self.state.armed)
            if prev_state.mode != self.state.mode:
                rospy.loginfo("Current mode: %s" % self.state.mode)
                prev_state = self.state
            rate.sleep()
        rospy.Subscriber('/mavros/global_position/local', Odometry, self.callback)
        rospy.Subscriber("parcel/position", PoseStamped, self.aktarget)
        rospy.Subscriber("/mavros/global_position/compass_hdg", Float64, self.rot)
        self.usecamera = False
        self.xy_alt = [100, 100, 100]
        self.packetfound = False
        rospy.loginfo("Fliege ueber Paket")
        self.target.pose.position.x = 2
        self.target.pose.position.y = 2
        self.target.pose.position.z = 2
        yaw = radians(90)
        quaternion = quaternion_from_euler(0, 0, yaw)
        self.target.pose.orientation = Quaternion(*quaternion)
        self.twist = 0
        self.listener()

    def rot(self, twist):
        self.twist = radians(-twist.data + 90)

    def state_cb(self, state):
        self.state = state

    def callback(self, data):
        self.aktpos = data
        if not self.usecamera:
            rospy.loginfo((data.pose.pose.position.x - self.target.pose.position.x) * (
                        data.pose.pose.position.x - self.target.pose.position.x) + (
                                      data.pose.pose.position.y - self.target.pose.position.y) * (
                                      data.pose.pose.position.y - self.target.pose.position.y))

        if (data.pose.pose.position.x - self.target.pose.position.x) * (
                data.pose.pose.position.x - self.target.pose.position.x) + (
                data.pose.pose.position.y - self.target.pose.position.y) * (
                data.pose.pose.position.y - self.target.pose.position.y) < 1 and data.pose.pose.position.z > 1.6 and not self.usecamera:
            self.usecamera = True
            rospy.loginfo("Cameraerkennung aktiviert")
        self.local_pos_pub.publish(self.target)

    def aktarget(self, data):
        if self.usecamera and (self.xy_alt[0] - self.aktpos.pose.pose.position.x) * (
                self.xy_alt[0] - self.aktpos.pose.pose.position.x) + (
                self.xy_alt[1] - self.aktpos.pose.pose.position.y) * (
                self.xy_alt[1] - self.aktpos.pose.pose.position.y) < 0.001:

            x = - cos(self.twist) * (data.pose.position.y - 104) / 200 + sin(self.twist) * (
                        data.pose.position.x - 160) / 200
            y = - cos(self.twist) * (data.pose.position.x - 160) / 200 - sin(self.twist) * (
                        data.pose.position.y - 104) / 200

            if x < 0.05 and y < 0.05 and fabs(self.xy_alt[2] - self.aktpos.pose.pose.position.z) < 0.05:
                if self.aktpos.pose.pose.position.z < 0.6 or self.packetfound:
                    yaw = self.twist - radians(data.pose.position.z) * 0.2
                    quaternion = quaternion_from_euler(0, 0, yaw)
                    self.target.pose.orientation = Quaternion(*quaternion)
                    rospy.loginfo([fabs(self.winkelbeschleunigung - data.pose.position.z),
                                   fabs((self.twist / np.pi * 180) - data.pose.position.z)])

                    if fabs(self.winkelbeschleunigung - data.pose.position.z) < 3 and fabs(data.pose.position.z) < 3:
                        rospy.loginfo("gedreht")
                        rospy.loginfo(self.aktpos.pose.pose.position.z)
                        if self.aktpos.pose.pose.position.z > 0.3 and not self.packetfound:
                            self.target.pose.position.z = self.aktpos.pose.pose.position.z - 0.1
                        else:
                            self.target.pose.position.z = 0.2
                            self.packetfound = True
                            rospy.loginfo("Paket gefunden und GEDREHT!!!")
                    self.winkelbeschleunigung = data.pose.position.z

                if self.aktpos.pose.pose.position.z > 0.6:
                    rospy.loginfo("vermindere z")
                    self.target.pose.position.z = self.aktpos.pose.pose.position.z - 0.1
            if self.aktpos.pose.pose.position.z < 0.4:
                x = x / 2
                y = y / 2
            self.target.pose.position.x = self.aktpos.pose.pose.position.x + x
            self.target.pose.position.y = self.aktpos.pose.pose.position.y + y
        self.xy_alt = [self.aktpos.pose.pose.position.x, self.aktpos.pose.pose.position.y,
                       self.aktpos.pose.pose.position.z]

    def listener(self):
        rospy.spin()


if __name__ == '__main__':
    fc = FlightController()
