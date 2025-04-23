#! /usr/bin/env python3

#Make a node an executable node
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/publisherstr.py

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

rospy.init_node("publishword")
#1st argument: topic name
#2nd argument: message type 
#3rd argument: queue_size

# pub = rospy.Publisher("/words", String, queue_size=10)
# msg = " Helloooo"
# rate = rospy.Rate(10)

pub = rospy.Publisher("/words", Int64, queue_size=10)
msg = Int64()
msg.data = 3
rate = rospy.Rate(10)

#Press ctrl+x to terminate the node
while not rospy.is_shutdown():
	print(msg)
	pub.publish(msg)
	rate.sleep()
