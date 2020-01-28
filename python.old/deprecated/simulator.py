import rospy
import cv2
from std_msgs.msg import String


def nothing(x):
    pass


def createMsg(type, value):
    return "%s:%d" % (type, value)


def talker():
    rospy.loginfo("simulator Start")

    cv2.namedWindow("Simulator")

    cv2.createButton("up", 0, 179, nothing)
    cv2.createButton("left", 0, 255, nothing)
    cv2.createButton("down", "Trackbars", 0, 255, nothing)
    cv2.createButton("right", 179, 179, nothing)
    cv2.createTrackbar("Ziel x", 10, 10, nothing)
    cv2.createTrackbar("Ziel y", 10, 10, nothing)

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
