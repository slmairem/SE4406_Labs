#!/usr/bin/env python3

import rospy
import sys
from geometry_msgs.msg import Twist

# Komut satırından turtle ID al
nodeid = str(sys.argv[1])
nodename = 'turtle' + nodeid

def movetask():
    speed = 0.3 
    distance = 4.0  
    direction = -1  

    vel_msg = Twist()
    vel_msg.linear.x = direction * abs(speed)
    vel_msg.angular.z = 0.0

    t0 = rospy.Time.now().to_sec()
    curr_dist = 0.0
    rate = rospy.Rate(10)

    while curr_dist < distance and not rospy.is_shutdown():
        pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        curr_dist = abs(speed) * (t1 - t0)
        rate.sleep()

    # Durdur
    vel_msg.linear.x = 0
    pub.publish(vel_msg)

# ROS node başlat
rospy.init_node("movenode", anonymous=True)
pub = rospy.Publisher(nodename + "/cmd_vel", Twist, queue_size=10)

# Görevi çalıştır
movetask()

