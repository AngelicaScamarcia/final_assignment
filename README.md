# Final_assignment


This is the third assignment of the Research Track 1 course. 
The target of the project is to drive a robot in a 3D map, thanks to a Python code.
Furthermore the user can control the robot, choosing one of the following choices:
1. provide the robot with coordinates x and y that it reaches automatically 
2. drive the robot by the keyboard
3. drive the robot by the keyboard avoiding obstacles
 

Installing and running
----------------------

You have to download the repository from https://github.com/CarmineD8/final_assignment.git (github.com) and https://github.com/CarmineD8/slam_gmapping.git (github.com).

After downloading and building the environment, make the ' .py ' file executable with the command:

```bash
$ chmod +x <name_of_the_script>.py
```

To run the simulation use the following command in three different terminal:

```bash
$ roslaunch final_assignment simulation_gmapping.launch
```

```bash
$ roslaunch final_assignment move_base.launch
```

```bash
$ roslaunch a_assignment3 a_launch.launch
```

Now you can see the robot starts to move in the environment.


Structer of the code
---------

The logic behind the code is shown in the attached flowchart. 

So you have the script ' a_launch.launch ' which contain ' controller.py ', where you can find the functions to manage each user choice, and ' case_2.py '.

There are 4 type of choices:

1. if the user select the first choice, he must enter X and Y coordinates with which the robot can move towards a defined position; moreover the code is able to show a message which inform the user if the target is achieved or not

2. if the user select the second choice, the code called the function ' teleop_twist_keyboard ' which is the main responsible of the robot's moves

3. if the user select the third choice, the code called the function ' teleop_twist_keyboard ' which is the main responsible of the robot's moves, plus the collision handler which allow to the robot to avoid obstacles and proceed along the path smoothly

4. in the last choice, the user simply close the whole program.


Something about the simulator
---------

This assignment relies on some software facilities, like:

1. Gazebo, which is an open-source 3D robotic simulator integrated into ROS that has the ability to accurately simulate robots in indoor and outdoor environments. In particular, in this case, the robot surfs in a group of rooms delimited by walls. For controlling the robot I need some topics like ' /scan ' (topic on which the simulation node publishes the output of the robot laser scanners) and ' /cmd_vel ' (topic to which the simulation node is subscribed in order to receive commands to set the robot linear and angular velocity).  

2. Rviz, which is a 3D viewer and It interacts with Gazebo

3. slam_gmapping (node), which is the node that implements a simultaneous localization and mapping (SLAM) algorithm

4. teleop_twist_keyboard (node), which is a GUI (Graphic User Interface) that allows the user to drive a robot by the keyboard.







