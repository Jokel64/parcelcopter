#! /usr/bin/env python2

import rospy 
import numpy as np
import cv2

from sub_topics.sub_zed_image_color import ZED_Image_Color
from sub_topics.sub_zed_depth_image import ZED_Depth_Image
from sub_topics.sub_zed_point_cloud import ZED_Point_Cloud
# from std_srvs.srv import Trigger, TriggerResponse
from object_det_srv_msg.srv import ObjectLocation, ObjectLocationResponse
from object_det_srv_msg.msg import PixLocation
from geometry_msgs.msg import Pose


class Object_det_color_server():
    def __init__(self, srv_name='/itm/zed_color_object_detection_service'):
        self._srv_name = srv_name
        self._obj_det_color_service = rospy.Service(self._srv_name, ObjectLocation, self.srv_callback)

        # subscribe three image resources 
        self._sub_Image = ZED_Image_Color()
        self._sub_Depth_Image = ZED_Depth_Image()
        self._sub_Point_Cloud = ZED_Point_Cloud()

        ## color filter setting 
        self._lower_blue = np.array([0, 182, 147])
        self._upper_blue = np.array([103, 255, 255])
        self._font = cv2.FONT_HERSHEY_SIMPLEX

        ## target 2D position 
        self.pos_2D = PixLocation()
        self.distance = 0.0
        self.pos_3D = Pose() # ref to left camera

        ## time 
        self.fps2D = 0.0
  

    def srv_callback(self, request):
        # call to cal the pix positin 
        self.object_detection()

        # response of the server
        response = ObjectLocationResponse()
        # string loc_type
        # ---
        # bool success
        # float64 distance
        # object_det_srv_msg/PixLocation pix_pos
        #   time timestamp
        #   int64[] pos
        # geometry_msgs/Pose pose
        #   geometry_msgs/Point position
        #     float64 x
        #     float64 y
        #     float64 z
        #   geometry_msgs/Quaternion orientation
        #     float64 x
        #     float64 y
        #     float64 z
        #     float64 w

        if -1 in self.pos_2D.pos:
            # just return false message
            response.success = False
        else:
            if request.loc_type=='2D':
                # just return 2D location (pixel)
                response.success = True
            # elif request.loc_type=='Point Cloud':
            #     # calculate the 3D position 
            #     self.position_Point_Cloud()
            #     response.success = True
            # elif request.loc_type=='Depth Image':
            #     self.distance_Depth_Image()
            #     response.success = True
            elif request.loc_type=='3D':
                # calculate the 3D position 
                self.position_Point_Cloud()
                self.distance_Depth_Image()
                response.success = True
            else:
                response.success = False
                rospy.loginfo('Please input the following service request=2D/3D')
        
        
        # set the data to response
        response.pix_pos.pos = self.pos_2D.pos
        response.pix_pos.timestamp = self.pos_2D.timestamp
        response.distance = self.distance
        response.pose = self.pos_3D 

        # reset all data
        self.reset_output()

        return response
       

    def object_detection(self):
        image = self._sub_Image.get_ZED_image() 
         # get the image from zed 
        if image is not None:
            t1 = cv2.getTickCount()
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self._lower_blue, self._upper_blue)
        
            result = cv2.bitwise_and(image, image, mask=mask)
            result = cv2.cvtColor(result,cv2.COLOR_HSV2BGR)
            result = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
            blurred = cv2.blur(result, (9,9))
            (_,threshold) = cv2.threshold(blurred,90,255, cv2.THRESH_BINARY)
            (_,cnts,h) = cv2.findContours(threshold.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            self.pos_2D.timestamp = rospy.Time.now()
        
            if len(cnts)>0:
                c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
                rect= cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)  # the same as int64
                # print(box)
                # pos = [xmin, ymin, xmax, ymax]
                self.pos_2D.pos = np.min(box, axis=0).tolist() + np.max(box, axis=0).tolist()
                # print(self.pos_2D.pos)
          
            else:
                self.pos_2D.pos = [-1] * 4
                # np.array(np.nan).repeat(4) 
        
            t2 = cv2.getTickCount()
            self.fps2D = cv2.getTickFrequency()/(t2-t1)
            cv2.imshow("color_test", image)

    
    def distance_Depth_Image(self):
        self.distance = self._sub_Depth_Image.get_target_distance(self.pos_2D.pos)
        
    
    def position_Point_Cloud(self):
        self.pos_3D = self._sub_Point_Cloud.get_target_position(self.pos_2D.pos)
        

    def reset_output(self):
        self.pos_2D.pos = [-1] * 4
        self.pos_2D.timestamp = np.nan
    
    

if __name__=="__main__":
    rospy.init_node('object_color_detect_service', log_level=rospy.INFO)
    obj_det_color_serv_object = Object_det_color_server()
    rospy.spin()
