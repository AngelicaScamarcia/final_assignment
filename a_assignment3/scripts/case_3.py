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

def callback_map(data):
    #callback to copy the remap_cmd_vel on repost which can be modified or left untouched
    global repost
    repost = data

def scan(ranges):
    #decompose the ranges in 3 parts and store the minimum distance for each of them
    
    distance= [0,0,0]
    right = ranges[0:240]
    center = ranges[240:480]
    left = ranges[480:721]
    
    R = min(right)
    F = min(mid)
    L = min(left)
    
    distance[0] = min(right)
    distance[1] = min(center)
    distance[2] = min(left)
    return distance
        
def callback_scan(data):
    global repost
    
    #initialize the publisher
    pub= rospy.Publisher('cmd_vel',Twist, queue_size=10)
    
    #compute the minimun obsable distance to the right, left and in front of the robot
    distances = minimum_th(data.ranges)
    if R < threshold :
        if repost.angular.z < 0 :
            #turn right   
            repost.angular.z = 0    
    
    if F < threshold:
        if repost.linear.x > 0 :
            #move towards the obstacle
            repost.linear.x = 0
    
    if L < threshold :
        if repost.angular.z > 0 :
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
    rospy.Subscriber("/scan", LaserScan, callback_scan)
    rospy.spin()
    
#main 
if __name__=="__main__":
    input_keyboard()
    
