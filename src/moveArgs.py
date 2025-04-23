#!/usr/bin/env python3

# rosrun turtlesim turtlesim_node __name:=&quot;turtle2&quot; turtle1:=/turtle2


import rospy
import sys
from geometry_msgs.msg import Twist

nodeid = str(sys.argv[1])  
nodename = 'turtle' + nodeid  

def movetask():
    rospy.init_node("movenode", anonymous=True)
    pub = rospy.Publisher(nodename + "/cmd_vel", Twist, queue_size=10)

    vel_msg = Twist()

    if nodeid == "1":
        # Düz ilerleyen turtle
        vel_msg.linear.x = 0.2
        vel_msg.angular.z = 0
    elif nodeid == "2":
        # Daire çizen turtle
        vel_msg.linear.x = 0.2  
        vel_msg.angular.z = 0.5  

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

    # Hareketi durdur
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

if __name__ == "__main__":
    movetask()

