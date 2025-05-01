#!/usr/bin/env python3

import rospy
import sys
from geometry_msgs.msg import Twist

def movetask():
    rospy.init_node("movenode", anonymous=True)

    nodeid=str(sys.argv[1])
    nodename='robot_'+nodeid

    pub = rospy.Publisher(nodename+"/cmd_vel", Twist, queue_size=10)

    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = 0.2

    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)


if __name__ == "__main__":
    movetask()

