# ROS performance test 
This repository provides example files for testing and comparing ROS nodes written in python and C++.

- Tested on Indigo
- ROS node files are placed in `src/` .
- Showing the results is done by running the plotter file in `scripts/`.

## Nodes
- C++ publisher node publishes to topic ``test_msg_cpp``
- Python publisher node publishes to topic ``test_msg_py``
- C++ and Python subscriber nodes both listen to both of these topics


In total there are four different combinations
- C++ publisher to Python subscriber
- C++ publisher to C++ subscriber
- Python publisher to Python subscriber
- Python publisher to C++ subscriber


## Method
- Everytime the callback of the subscriber is called, the current clock is recorded and compared to the previous clock call
- This comparison provides the loop rate on subscriber side and can be compared to the nominal publishing rate on publisher side
- In each subscriber, there is a counter to counter the number of calls to the callback function. Once this counter reaches `COUNTER_MAX`, all the recorded loop rates are written to a file in `data_saved/` directory
- The comparison of these four combinations can be shown by running `scripts/plot_results.py`

###Results

Three sample results for communication frequencies of **50 Hz**, **1 kHz** and **5 kHz** are placed in `data_saved/`.

## Run
- Both publisher nodes require a parameter called ``period``. This parameter can be given via rosparam server or via YAML files.
- You can either run via rosrun or roslaunch which uses the launch file included in `launch/` directory
