#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def movetask():
	rospy.init_node("movenode",anonymous=True)
	pub = rospy.Publisher("/turtle2/cmd_vel", Twist, queue_size=10 )
	vel_msg= Twist()
	vel_msg.linear.x= 123
	vel_msg.linear.y= 0
	vel_msg.linear.z= 0
	vel_msg.angular.x= 0
	vel_msg.angular.y= 0
	vel_msg.angular.z= 0
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
