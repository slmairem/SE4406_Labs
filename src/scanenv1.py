#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import sys 

nodeid=str(sys.argv[1])
nodename='robot_'+nodeid

def receiveSensorMsgs(msg):
	#for i in range(len(msg.ranges)):
	rospy.loginfo("%f", msg.ranges[135])
    

def movetask():

	vel_msg = Twist()
	vel_msg.linear.x = 0.2
	vel_msg.angular.z = 0.0

	rate = rospy.Rate(10)  # 10 Hz
	while not rospy.is_shutdown():
		pub.publish(vel_msg)
		rate.sleep()

	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	pub.publish(vel_msg)

rospy.init_node("movenode", anonymous=True)
pub = rospy.Publisher(nodename+"/cmd_vel", Twist, queue_size=10)
sub = rospy.Subscriber(nodename+"/base_scan", LaserScan, receiveSensorMsgs)

movetask()
rospy.spin()
