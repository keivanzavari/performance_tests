#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: Keivan Zavari 
"""

import rospy
import rospkg
from timeit import default_timer as timer
import numpy as np
from performance_tests.msg import SuperAwesome


# ----------------

COUNTER_MAX = 5000

# ----------------
elapsed_time_ = []
timer_begin_  = timer()

counter_  = 0

save_to_file_ = True
caller_id_ = 'py'
# ----------------

def saveToFile(list_to_save):
    file_name = 'subscriber_py_from_' + caller_id_ + '_publisher.txt'
    
    # get an instance of RosPack with the default search paths
    rospack = rospkg.RosPack()
    # get the folder path for the package where the measurement report is
    folder_name = rospack.get_path('performance_tests')

    file_path = folder_name + '/data_saved/' + file_name
    file = open(file_path, 'w')
    for item in list_to_save:
        file.write("%s\n" % item)



# ----------------

def elapsedTime(counter):
    global timer_begin_
    if (counter==0):
        # this is the first time I am called
        timer_begin_ = timer()
        return 0
    else:
        elapsed = timer() - timer_begin_
        timer_begin_ = timer()
        return elapsed


# ----------------
def measurePerformance():

    global counter_, COUNTER_MAX, elapsed_time_

    if (counter_ <= COUNTER_MAX):
        elapsed_time_.append(elapsedTime(counter_))
        counter_+=1
            
    else:
        counter_ = 0
        # elapsed_time_.remove(0)
        print COUNTER_MAX, ' times received messages... ' , np.mean(elapsed_time_)
        if (save_to_file_):
            saveToFile(elapsed_time_)
        # print(elapsed_time_)
        elapsed_time_ =[]

# ----------------

def callbackPy(data):
    # make sure incoming message is not empty 
    global caller_id_
    # if there is data
    if (data.data):
        caller_id_ = 'py'
        measurePerformance()

# ----------------

def callbackCpp(data):
    # make sure incoming message is not empty 
    global caller_id_
    # if there is data
    if (data.data):
        caller_id_ = 'cpp'
        measurePerformance()

# ----------------


def listen_for_messages():
    # topic name, checked with cv_camera
    topic_py = '/test_msg_py'
    topic_cpp = '/test_msg_cpp'
    rospy.loginfo('listening to two topics ' + topic_py + ', ' + topic_cpp)


    # start the subscriber
    sub_py = rospy.Subscriber(topic_py, SuperAwesome, callbackPy)
    sub_cpp = rospy.Subscriber(topic_cpp, SuperAwesome, callbackCpp)

    # keep python from exiting until this node is stopped 
    rospy.spin()


# ----------------

if __name__ == '__main__':
    try:
        
        # initialise the node
        node_name ='subscriber_py'
        rospy.init_node(node_name, anonymous=True)
        rospy.loginfo('initializing ' + node_name + ' node')


        listen_for_messages()

    except rospy.ROSInterruptException:
        pass

