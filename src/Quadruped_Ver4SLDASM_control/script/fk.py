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
    pub3 = rospy.Publisher('/Quadruped_Ver4SLDASM/FR_KNEE_ELBOW_position_controller/command',Float64, queue_size=5)
    pub2 = rospy.Publisher('/Quadruped_Ver4SLDASM/FR_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=5)
    pub1 = rospy.Publisher('/Quadruped_Ver4SLDASM/FR_SHOULDER_BASE_position_controller/command',Float64, queue_size=5)
    pub4 = rospy.Publisher('/Quadruped_Ver4SLDASM/BR_KNEE_ELBOW_position_controller/command',Float64, queue_size=5)
    pub5 = rospy.Publisher('/Quadruped_Ver4SLDASM/BR_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=5)
    pub6 = rospy.Publisher('/Quadruped_Ver4SLDASM/BR_SHOULDER_BASE_position_controller/command',Float64, queue_size=5)
    pub7 = rospy.Publisher('/Quadruped_Ver4SLDASM/BL_KNEE_ELBOW_position_controller/command',Float64, queue_size=5)
    pub8 = rospy.Publisher('/Quadruped_Ver4SLDASM/BL_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=5)
    pub9 = rospy.Publisher('/Quadruped_Ver4SLDASM/BL_SHOULDER_BASE_position_controller/command',Float64, queue_size=5)
    pub10 = rospy.Publisher('/Quadruped_Ver4SLDASM/FL_KNEE_ELBOW_position_controller/command',Float64, queue_size=5)
    pub11 = rospy.Publisher('/Quadruped_Ver4SLDASM/FL_ELBOW_SHOULDER_position_controller/command',Float64, queue_size=5)
    pub12 = rospy.Publisher('/Quadruped_Ver4SLDASM/FL_SHOULDER_BASE_position_controller/command',Float64, queue_size=5)
    rospy.init_node('fk_pub', anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
    	pos3= 1.3
    	pos2= 0.7
    	pos1= 0.0
        pos4= 1.3
        pos5= 0.7
        pos6= 0.0
        pos7= 1.3
        pos8= -0.7
        pos9= 0.0
        pos10= 1.3
        pos11= -0.7
        pos12= 0.0
    	rospy.loginfo(pos3)
    	rospy.loginfo(pos2)
    	rospy.loginfo(pos1)
    	pub3.publish(pos3)
    	pub4.publish(pos4)
    	pub7.publish(pos7)
        pub10.publish(pos10)
        pub2.publish(pos2)
        pub5.publish(pos5)
        pub8.publish(pos8)
        pub11.publish(pos11)
        pub1.publish(pos1)
        pub6.publish(pos6)
        pub9.publish(pos9)
        pub12.publish(pos12)
    	#rate.sleep()

if __name__ == '__main__':
	try:
		fk_pub()
	except rospy.ROSInterruptException:
	    pass 	
		 		


































































