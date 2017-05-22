#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: Keivan Zavari
"""

import rospy
from performance_tests.msg import SuperAwesome


# ----------------

def publish_msg():
    topic_name = 'test_msg_py'
    pub = rospy.Publisher(topic_name, SuperAwesome, queue_size=10)
    try:
        period = rospy.get_param('period', 5.0)
    except KeyError:
        period = 5.0
    rate_ = 1.0/period
    rate = rospy.Rate(rate_) # Hz
    rospy.loginfo('initialized publisher with rate ' + str(rate_) + ' [Hz]')


    msg = SuperAwesome()
    msg.data = 'test_msg_py'
    
    # we can even add an extra time stamp to the message 
    # to track the times it takes for its delivery
    # msg.stamp = rospy.get_rostime()

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

# ----------------

if __name__ == '__main__':
    try:
        
        # initialise the node
        node_name ='publisher_py'
        rospy.init_node(node_name, anonymous=True)
        rospy.loginfo('initializing ' + node_name + ' node')

        publish_msg()

    except rospy.ROSInterruptException:
        pass