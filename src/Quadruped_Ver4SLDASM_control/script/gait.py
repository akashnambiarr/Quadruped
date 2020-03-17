#!/usr/bin/env python
import math
import rospy
import numpy as np
def fk_fl(th1,th2,th3):

	print "angle of elbow_shoulder=",(th2)
	print "angle of knee_elbow=",(th3)
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
	
	def ik_fl(Px,Py,Pz):
		
		px=Px-32
		py = Py+223
		pz =Pz-463 

		l1=324.17
		l2=324.17
		t1=(math.atan(py/px))
		#print "t1=",math.degrees(t1)
		k = px**2 + py**2 + pz**2
		#print "k=",k
		cb=(k-(l1**2+l2**2))/(2*l1*l2)
		#print "cb=",cb
		sb=math.sqrt(1-cb**2)
		#print"sb=",sb
		B=(math.atan2(sb,cb))
		#print "B=",math.degrees((B))

		e1 = np.array([[px*math.cos(t1)+py*math.sin(t1)],[pz]])
		#print "e1=",e1
		e2 = np.array([[(l2*math.cos(B)+l1),-l2*math.sin(B)],[l2*math.sin(B),(l2*math.cos(B)+l1)]])
		#print "e2=",e2
		ei=np.linalg.inv(e2)
		#print "eInv",ei
		e3 = np.dot(ei,e1)
		#print "e3",e3
		G=math.atan((e3[1,0])/e3[0,0])
		#print "G=",G
		a=G-math.radians(180)
		#print "a=",a
		t2=(a-math.radians(164.25))

		if (t2<-4.36) and (t2>-6.28):
			t2=t2+math.radians(360)
		else:
			t2=-(t2+math.radians(378))


		t3=(B-math.radians(31.5))
		print "Theta 1=",math.degrees(t1)
		print "Theta 2=",math.degrees(t2)
		print "Theta 3=",math.degrees(t3)

	ik_fl(Px,Py,Pz)

fk_fl(0,56,30)
