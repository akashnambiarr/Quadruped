#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64 
from tf2_msgs.msg import TFMessage
import math
import tf
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Pose

from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from geometry_msgs.msg import Pose


def fk_pub():
    pub4 = rospy.Publisher('/Quadruped_Ver4SLDASM/BR_KNEE_ELBOW_position_controller/command',Float64, queue_size=10)
    pub5 = rospy.Publisher('/Quadruped_Ver4SLDASM/BR_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=10)
    pub6 = rospy.Publisher('/Quadruped_Ver4SLDASM/BR_SHOULDER_BASE_position_controller/command',Float64, queue_size=10)
    pub10 = rospy.Publisher('/Quadruped_Ver4SLDASM/FL_KNEE_ELBOW_position_controller/command',Float64, queue_size=10)
    pub11 = rospy.Publisher('/Quadruped_Ver4SLDASM/FL_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=10)
    pub12 = rospy.Publisher('/Quadruped_Ver4SLDASM/FL_SHOULDER_BASE_position_controller/command',Float64, queue_size=10)
    pub7 = rospy.Publisher('/Quadruped_Ver4SLDASM/BL_KNEE_ELBOW_position_controller/command',Float64, queue_size=10)
    pub8 = rospy.Publisher('/Quadruped_Ver4SLDASM/BL_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=10)
    pub9 = rospy.Publisher('/Quadruped_Ver4SLDASM/BL_SHOULDER_BASE_position_controller/command',Float64, queue_size=10)
    pub3 = rospy.Publisher('/Quadruped_Ver4SLDASM/FR_KNEE_ELBOW_position_controller/command',Float64, queue_size=10)
    pub2 = rospy.Publisher('/Quadruped_Ver4SLDASM/FR_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=10)
    pub1 = rospy.Publisher('/Quadruped_Ver4SLDASM/FR_SHOULDER_BASE_position_controller/command',Float64, queue_size=10)
    rospy.init_node('fk_pub', anonymous=True)
    rate=rospy.Rate(10)
    for r in range (10):
        #BR
        while not rospy.is_shutdown():
            for t in range(5):
                pos4= 1.2
                pos5= 0.0
                pos6= 0.0
                rospy.loginfo(pos4)
                rospy.loginfo(pos5)
                rospy.loginfo(pos6)
                pub4.publish(pos4)
                pub5.publish(pos5)
                pub6.publish(pos6)
                rate.sleep()
                pos4= 1.7
                pos5= 0.4
                pos6= 0.0
                rospy.loginfo(pos4)
                rospy.loginfo(pos5)
                rospy.loginfo(pos6)
                pub4.publish(pos4)
                pub5.publish(pos5)
                pub6.publish(pos6)
            break
        rospy.sleep(0.1) 

        #move
        while not rospy.is_shutdown():
            for f in range(5):
                pos4= 1.3
                pos5= 0.7
                pos6= -0.3
                pub4.publish(pos4)
                pub5.publish(pos5)
                pub6.publish(pos6)
            break
        rospy.sleep(0.2)
        pos6= 0.0
        pub6.publish(pos6)
        #FL
        while not rospy.is_shutdown():
            for u in range(5):
                pos10= 1.6
                pos11= -1.8
                pos12= 0.0
                pub10.publish(pos10)
                pub11.publish(pos11)
                pub12.publish(pos12)
                rate.sleep()
                pos10= 2.1
                pos11=-1.2
                pos12= 0.0
                pub10.publish(pos10)
                pub11.publish(pos11)
                pub12.publish(pos12)    
            break
        rospy.sleep(0.3)  
        #move
        while not rospy.is_shutdown():
            for p in range(5):
                pos10= 1.4
                pos11= -0.5
                pos12= 0.3
                pub10.publish(pos10)
                pub11.publish(pos11)
                pub12.publish(pos12)
            break
        rospy.sleep(0.2)
        pos12= 0.0
        pub12.publish(pos12)


                #bl
        while not rospy.is_shutdown():
            for o in range(5):
                pos7= 1.2
                pos8= 0.0
                pos9= 0.0
                rospy.loginfo(pos7)
                rospy.loginfo(pos8)
                rospy.loginfo(pos9)
                pub7.publish(pos7)
                pub8.publish(pos8)
                pub9.publish(pos9)
                rate.sleep()
                pos7= 1.7
                pos8=-0.4
                pos9= 0.0
                pub7.publish(pos7)
                pub8.publish(pos8)
                pub9.publish(pos9)
            break
        rospy.sleep(0.1)  
        #move
        while not rospy.is_shutdown():
            for p in range(5):
                pos7= 1.3
                pos8= -0.7
                pos9= -0.3
                pub7.publish(pos7)
                pub8.publish(pos8)
                pub9.publish(pos9)   
            break
        rospy.sleep(0.2)
        pos9= 0.0
        pub9.publish(pos9)
           #FR
        while not rospy.is_shutdown():
            for j in range(5):
                pos3= 1.6
                pos2= 1.8
                pos1= 0.0
                rospy.loginfo(pos3)
                rospy.loginfo(pos2)
                rospy.loginfo(pos1)
                pub3.publish(pos3)
                pub2.publish(pos2)
                pub1.publish(pos1)
                rate.sleep()
                pos3= 2.1
                pos2= 1.2
                pos1= 0.0
                rospy.loginfo(pos4)
                rospy.loginfo(pos5)
                rospy.loginfo(pos6)
                pub3.publish(pos3)
                pub2.publish(pos2)
                pub1.publish(pos1)
            break  
        rospy.sleep(0.3) 
        #move
        while not rospy.is_shutdown():
            for u in range(5):
                pos3= 1.4
                pos2= 0.5
                pos1= 0.3
                pub3.publish(pos3)
                pub2.publish(pos2)
                pub1.publish(pos1)
            break 
        rospy.sleep(0.2)
        pos1= 0.0
        pub1.publish(pos1)




if __name__ == '__main__':
    try:
        fk_pub()
    except rospy.ROSInterruptException:
        pass    