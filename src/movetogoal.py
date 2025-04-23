#! /usr/bin/env python3

#Make a python node executable
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/movetogoal.py 

import rospy
import sys
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

nodeid = str(sys.argv[1])
nodename = 'turtle' + nodeid

class Turtlebot: 

	def __init__(self):
		rospy.init_node('turtletogoal', anonymous=True)
		self.pub = rospy.Publisher(nodename+'/cmd_vel', Twist, queue_size=10)
		self.sub = rospy.Subscriber(nodename+'/pose', Pose, self.update_pose)
		self.pose = Pose()
		self.rate = rospy.Rate(10)

	def update_pose(self, data):
		self.pose = data

	def euclidean_distance(self, goal_pose):
		return sqrt(pow((goal_pose.x - self.pose.x), 2)+pow((goal_pose.y - self.pose.y), 2))

	def linear_vel(self, goal_pose, constant=1.5):
		return constant * self.euclidean_distance(goal_pose)		

	def steering_angle(self, goal_pose):
		return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

	def angular_vel(self, goal_pose, constant=6):
		return constant * (self.steering_angle(goal_pose)-self.pose.theta)
	
	def move2goal(self):
		goal_pose = Pose()
		if nodeid == "1":
			goal_pose.x = 2
			goal_pose.y = 2
		else:
			goal_pose.x = 5
			goal_pose.y = 5
		tolerance = 0.1

		vel_msg = Twist()
		while self.euclidean_distance(goal_pose) >= tolerance:
			vel_msg.linear.x = self.linear_vel(goal_pose)
			vel_msg.angular.z = self.angular_vel(goal_pose)
			self.pub.publish(vel_msg)
			self.rate.sleep()
		# to stop the robot
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.pub.publish(vel_msg)
		rospy.spin()

if __name__ == "__main__":
	try:
		x = Turtlebot()
		x.move2goal()

	except rospy.ROSInterruptException:
		pass









