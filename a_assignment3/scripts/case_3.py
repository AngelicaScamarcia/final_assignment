#! /usr/bin/env python

import rospy
import numpy
from geometry_msgs.msg import Twist, Vector3    #for cmd_vel topic
from sensor_msgs.msg import LaserScan           #for scan topic

#limit distance to avoid collision
threshold = 0.5

#initialize a Twist object for the publisher
init = Vector3(0, 0, 0)
repost = Twist( init, init)

def callback_map(msg):
    #callback to copy the remap_cmd_vel on repost which can be modified or left untouched
    global repost
    repost = msg

def scan(msg):
    #decompose the ranges in 3 parts and store the minimum distance for each of them
    global repost
    pub= rospy.Publisher('cmd_vel',Twist, queue_size=10)
    distance=  {
    'R': min(min(msg.ranges[144:287]), 10),
    'F': min(min(msg.ranges[288:431]), 10),
    'L': min(min(msg.ranges[432:575]), 10),
    }
        
    #compute the minimun obsable distance to the right, left and in front of the robot
    if distance['R'] < threshold :
            #turn right   
            repost.angular.z = 0    
    
    elif distance['F'] < threshold:        
            #move towards the obstacle
            repost.linear.x = 0
    
    elif distance['L'] < threshold :
            #turn left 
            repost.angular.z = 0
    
    #pubblic on topic cmd_vel to the robot
    pub.publish(repost)

def input_keyboard():
    #initialize the node
    rospy.init_node('kb_map_node')
    #subscriber to topic remap_cmd_vel    
    rospy.Subscriber("/remap_cmd_vel", Twist, callback_map)
    #subscriber to topic scan
    rospy.Subscriber("/scan", LaserScan, scan)
    rospy.spin()
    
#main 
if __name__=="__main__":
    input_keyboard()
    
