# ROS performance test 
This repository provides example files for testing and comparing ROS nodes written in python and C++.

C++ files are in src directory while Python files live in scripts/.

## Nodes
- C++ publisher node publishing on topic ``test_msg_cpp``
- Python publisher node publishing on topic ``test_msg_py``
- C++ subscriber node listening to these topics
- Python subscriber node listening to these topics

### Parameters
- Both publisher nodes require a parameter called ``period``. This parameter can be given via rosparam server or via YAML files.

## Run
- You can either run via rosrun or roslaunch which uses the launch file included in `launch/` directory
