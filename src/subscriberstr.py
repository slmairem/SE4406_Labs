#! /usr/bin/env python3

#Make a node an executable node
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/subscriberstr.py

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

def receivemsg(msg):
	double = msg.data*2
	print(double)

rospy.init_node("subscriberword")

#1st argument: topic name
#2nd argument: message type 
#3rd argument: callback function
# sub = rospy.Subscriber("/words", String, receivemsg)

sub = rospy.Subscriber("/words", Int64, receivemsg)

rospy.spin()
