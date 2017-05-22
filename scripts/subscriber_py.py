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
elapsed_time = []
timer_prv_  = timer()

counter_  = 0

counter_max_ = 5
# ----------------

def elapsedTime(counter):
    global timer_prv_
    if (counter==0):
        # this is the first time I am called
        timer_prv_ = timer()
        return 0
    else:
        timer_ = timer() - timer_prv_
        timer_prv_ = timer()
        return timer_

def callbackPy(data):
    # make sure incoming message is not empty 
    global counter_, counter_max_, elapsed_time
    # rospy.loginfo(data.data)
    # if there is data
    if (data.data):
        if (counter_ <= counter_max_):
            elapsed_time.append(elapsedTime(counter_))
            counter_+=1
            print(elapsed_time)
        else:
            counter_ = 0
            elapsed_time.remove(0)
            print '5 times received, average: ', np.mean(elapsed_time)
            elapsed_time =[]



# def callbackCpp(data):
#     print data.data

def listen_for_messages():
    # topic name, checked with cv_camera
    topic_py = '/test_msg_py'
    topic_cpp = '/test_msg_cpp'
    rospy.loginfo('listening to two topics ' + topic_py + ', ' + topic_cpp)


    # start the subscriber
    lis_py = rospy.Subscriber(topic_py, SuperAwesome, callbackPy)
    # lis_cpp = rospy.Subscriber(topic_py, SuperAwesome, callbackCpp)

    # keep python from exiting until this node is stopped 
    rospy.spin()

if __name__ == '__main__':
    try:
        
        # initialise the node
        node_name ='subscriber_py'
        rospy.init_node(node_name, anonymous=True)
        rospy.loginfo('initialising ' + node_name + ' node')


        listen_for_messages()

    except rospy.ROSInterruptException:
        pass

