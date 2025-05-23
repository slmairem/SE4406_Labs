#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def movetask():
	rospy.init_node("movenode",anonymous=True)
	# spub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10 )
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10 )
	vel_msg= Twist()
	vel_msg.linear.x= 0.2
	vel_msg.linear.y= 0
	vel_msg.linear.z= 0
	vel_msg.angular.x= 0
	vel_msg.angular.y= 0
	vel_msg.angular.z= 0.2
	rate = rospy.Rate(10)# 10hz
	while not rospy.is_shutdown():
		pub.publish(vel_msg)
		rate.sleep()
	#stop the robot
	vel_msg.linear.x= 0
	vel_msg.angular.z= 0
	pub.publish(vel_msg)
	#pub.publish(vel_msg)

movetask()
