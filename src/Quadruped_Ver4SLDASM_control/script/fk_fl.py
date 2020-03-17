#!/usr/bin/env python
import math
import rospy
import numpy as np
# def fk_f1(th1,th2,th3):
th1=0
th2=22.91
th3=97.40
print "angle of elbow_shoulder=",math.radians(th2)
print "angle of knee_elbow=",math.radians(th3)
l1=324.17
l2=324.17
A=th2+164.25
B=th3+31.5
c1=math.cos(math.radians(th1))
OT4=np.array([[math.cos(math.radians(th1))*math.cos(math.radians(A+B)), -math.cos(math.radians(th1))*math.sin(math.radians(A+B)), math.sin(math.radians(th1)), (l2*math.cos(math.radians(th1))*math.cos(math.radians(A+B)))+(l1*math.cos(math.radians(A))*math.cos(math.radians(th1)))+32],[math.sin(math.radians(th1))*math.cos(math.radians(A+B)), -math.sin(math.radians(th1))*math.sin(math.radians(A+B)), -math.cos(math.radians(th1)), (l2*math.sin(math.radians(th1))*math.cos(math.radians(A+B)))+(l1*math.cos(math.radians(A))*math.sin(math.radians(th1)))-223],[math.sin(math.radians(A+B)), math.cos(math.radians(A+B)), 0, (l2*math.sin(math.radians(A+B)))+(l1*math.sin(math.radians(A)))+463],[0, 0, 0, 1]])
	#print (OT4)
Px=OT4[0,3]
Py=OT4[1,3]
Pz=OT4[2,3]
print "x Coordinate=",Px
print "y Coordinate=", Py
print "z Coordinate=", Pz
	
#fk_f1(0,56,30)





