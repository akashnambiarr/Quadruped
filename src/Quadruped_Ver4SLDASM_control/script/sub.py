#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64 

# class robot:
# 	def __init__(self):
# 		self.blknee= None
# 		print "hi"


def server(msg):
	
	print "hi"

	# def print_value(self):
	# 	if self.blknee is not None:
	# 		print "h22"
	
if __name__ == '__main__':
	rospy.init_node('fk_sub', anonymous=True)
	# Robot= robot()
	rospy.Subscriber('/Quadruped_Ver4SLDASM/FR_KNEE_ELBOW_position_controller/command',Float64,server)
	rospy.spin()
	