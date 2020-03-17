#!/usr/bin/env python

import rospy 
import math 	
from std_msgs.msg import Float64 
from geometry_msgs.msg import Pose
import tf2_ros
def fk_pub():
	pub = rospy.Publisher('/tf',Pose, queue_size=10)
	rospy.init_node('fk_pub', anonymous=True)
	pose_msg= Pose()
	pose.msg.position.x=0
	pose_msg.position.y=0
	pose.msg.position.z=0

	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		pos= 5.0
		rospy.loginfo(pos)
		pub.publish(pos)
		rate.sleep()

if __name__ == '__main__':
	try:
		fk_pub()
	except rospy.ROSInterruptException:
	    pass 	
		 		
