#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
KEIVAN . ZAVARI @ GMAIL.COM
"""

import rospy
from timeit import default_timer as timer
import numpy as np
from performance_tests.msg import SuperAwesome


# ----------------

COUNTER_MAX = 5000

# ----------------
elapsed_time = []
t2  = timer()

counter_  = 0

save_to_file_ = True
caller_id = 'py'
# ----------------

def saveToFile(list_to_save):
    file_name = 'subscriber_py_from_' + caller_id + '_publisher.txt'
    file = open(file_name, 'w')
    for item in list_to_save:
        file.write("%s\n" % item)



# ----------------

def elapsedTime(counter):
    global t2
    if (counter==0):
        # this is the first time I am called
        t2 = timer()
        return 0
    else:
        elapsed = timer() - t2
        t2 = timer()
        return elapsed


# ----------------
def measurePerformance():

    global counter_, COUNTER_MAX, elapsed_time

    if (counter_ <= COUNTER_MAX):
        elapsed_time.append(elapsedTime(counter_))
        counter_+=1
            
    else:
        counter_ = 0
        # elapsed_time.remove(0)
        print COUNTER_MAX, ' times received messages... ' , np.mean(elapsed_time)
        if (save_to_file_):
            saveToFile(elapsed_time)
        # print(elapsed_time)
        elapsed_time =[]

# ----------------

def callbackPy(data):
    # make sure incoming message is not empty 
    global caller_id
    # if there is data
    if (data.data):
        measurePerformance()
        caller_id = 'py'

# ----------------

def callbackCpp(data):
    # make sure incoming message is not empty 
    global caller_id
    # if there is data
    if (data.data):
        measurePerformance(data.data)
        caller_id = 'cpp'

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
        rospy.loginfo('initialising ' + node_name + ' node')


        listen_for_messages()

    except rospy.ROSInterruptException:
        pass

