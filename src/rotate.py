#!/usr/bin/env python3

# rosrun turtlesim turtlesim_node __name:=&quot;turtle2&quot; turtle1:=/turtle2
# chmod u+x ~/catkin_ws/src/beginner_tutorials/src/publisherstr.py

import rospy
import sys
from geometry_msgs.msg import Twist
import math

nodeid = str(sys.argv[1])  
nodename = 'turtle' + nodeid
vel_msg = Twist()

vel_msg.linear.x = 0
vel_msg.angular.z = 0

rospy.init_node("rotatenode", anonymous=True)
pub = rospy.Publisher(nodename + "/cmd_vel", Twist, queue_size=10)
rate = rospy.Rate(10)  # 10 Hz

def rotatetask(speed, angle, clockwise, lspeed=0):
	angularspeed = speed * (math.pi/180.0)
	relativeAngle = angle * (math.pi/180.0)

	vel_msg.linear.x = lspeed
	vel_msg.angular.z = clockwise * angularspeed
	
	t0 = rospy.Time.now().to_sec()
	currAngle = 0
	while(currAngle < relativeAngle):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		currAngle = angularspeed * (t1-t0)
		rate.sleep()
	# to stop the robot
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	pub.publish(vel_msg)
	
	
#rotatetask(speed,angle,clockwise,lspeed=0):
rotatetask(30,90, -1) # -1 = counterclockwise, 1 clockwise

	

