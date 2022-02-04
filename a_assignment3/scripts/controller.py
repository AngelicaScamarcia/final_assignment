#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import *
from actionlib_msgs.msg import *
from a_assignment3.srv import Kb_input   	       #service for 2 and 3


def first_choice():
    
    print("choice 1")
    x = float(input("insert x: "))
    y = float(input("insert y: "))
    
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    
    #waiting for the connection with the server
    client.wait_for_server()
    
    #create the goal
    goal = MoveBaseGoal()
    
    #set the goal parameter
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.orientation.w = 1
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    
    #send the goal
    client.send_goal(goal)
    finished_within_time = client.wait_for_result(rospy.Duration(30.0))
    if not finished_within_time:
        client.cancel_goal()
        rospy.loginfo("the robot couldn't achieve it")
        return -1
    else:
        rospy.loginfo("the robot reached the new position")
        return 1 


#call the keyboard service to menage the situation         	
def second_choice():
    #if the user selects mode 2 it will send 1 to the manage(req) function in case_2.py
    print("choice 2")
    
    rospy.wait_for_service('kb_input')
    kb_input = rospy.ServiceProxy('kb_input', Kb_input)
    kb_input(1)

def third_choice():
    #if the user selects mode 3 it will send 2 to the manage(req) function in case_2.py
    print("choice 3")
    
    rospy.wait_for_service('kb_input')
    kb_input = rospy.ServiceProxy('kb_input', Kb_input)
    kb_input(2)
    
def user():
    print("Please enter your choice ")
    print(" 1 . autonomously reach x,y coordinate provided by the user ")
    print(" 2 . drive the robot ")
    print(" 3 . drive the robot using the keyboard, collision handler active ")
    print(" 4 . quit the program: ")
    print()	
    return input("Please your choice should be entered here!: ")
      
 
if __name__=="__main__":
    #initialize ros node
    rospy.init_node('controller')
    flag = 1
    
    while(flag):
        choice = user()
        if (choice == '1'):
            first_choice()
            
        elif (choice == '2'):
            second_choice()  
            
        elif (choice == '3'):
            third_choice()
            
        elif (choice == '4'):
            flag = 0
            print("press ctrl-C to quit")
                           
        else:
            print("wrong input!!")
        
            
