#! /usr/bin/env python

import rospy
from a_assignment3.srv import Kb_input	
import os   

def manage(req):
    #read the request and then the function chose to call case 2 or 3
    if req.kb_case == 1:
       #call the launcher for case 3 (keyboard teleop)
       os.system("roslaunch a_assignment3 case_2.launch") 
       
    elif req.kb_case == 2:
        #call keyboard teleop and obstacle avoidance 
        print("call teleop twist keyboard")
        #call the launcher for case 3
        os.system("roslaunch a_assignment3 case_3.launch")
    
    else:
        print("wrong input")
    return 0         
   
   
def input_keyboard_server():  
    # define some information about the node 
    print("keyboard controlling for robot")
    #initialize the node
    rospy.init_node('keyboard_controller')
    
    #call server service 
    service = rospy.Service('kb_input', Kb_input , manage)
    print("service ready")
    rospy.spin()

#main
if __name__=="__main__":
    input_keyboard_server()
