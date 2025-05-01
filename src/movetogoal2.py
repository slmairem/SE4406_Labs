#! /usr/bin/env python

#Make a python node executable
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/movetogoal2.py

import rospy 
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math
from math import pow, atan2, sqrt
from tf.transformations import euler_from_quaternion, quaternion_from_euler

#nodeid=str(sys.argv[1])
#nodename="/robot_"+nodeid

class Turtlebot: 
	
	def __init__(self):
		

	def update_pose(self, data):
		

	def euclidean_distance(self, goal_pose):
		return sqrt(pow((goal_pose.position.x-self.pose.position.x),2)+pow((goal_pose.position.y-self.pose.position.y),2))

	def linear_vel(self, goal_pose, constant=0.1):
		return constant * self.euclidean_distance(goal_pose)

	def steering_angle(self, goal_pose):
		return atan2(goal_pose.position.y-self.pose.position.y, goal_pose.position.x-self.pose.position.x)

	def angular_vel(self, goal_pose, constant=0.5):
		return constant * (self.steering_angle(goal_pose)-self.yaw)

	def move2goal(self):
		newodom = Odometry()
		goal_pose = newodom.pose.pose
		goal_pose.position.x = input("x: ")
		goal_pose.position.y = input("y: ")
		dist_tolerance = input("tolerance: ")
		
		vel_msg = Twist()
		
		while self.euclidean_distance(goal_pose) >= dist_tolerance:
			
			vel_msg.linear.x = self.linear_vel(goal_pose)
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = self.angular_vel(goal_pose)

			print(str(self.pose.position.x), str(self.pose.position.y))
			self.vel_publisher.publish(vel_msg)
			self.rate.sleep()		
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.vel_publisher.publish(vel_msg)
		rospy.spin()

if __name__ == "__main__":
	try:
		x = Turtlebot()
		x.move2goal()

	except rospy.ROSInterruptException:
		pass








