
#include <ros/ros.h>
#include <performance_tests/SuperAwesome.h>


// -----------------------------------
performance_tests::SuperAwesome message;
// define the publisher
ros::Publisher pub;
// -----------------------------------


void callback1(const ros::TimerEvent&)
{
    // we can even add an extra time stamp to the message 
    // to track the times it takes for its delivery
    // message.stamp = ros::Time::now();

    pub.publish(message);

}

int main( int argc, char** argv )
{
    // initialize the node and define handle
    ros::init(argc, argv, "publisher_cpp");
    ros::NodeHandle n;

    pub = 
    n.advertise<performance_tests::SuperAwesome>("test_msg_cpp", 1);
    message.data = "string_message";

    double period;
    n.getParam("period",period);

    // check if block_position_z_ is given
    if ( !n.getParam("period",period)){
        period = 1;
        ROS_INFO("setting period to 1 [sec]");
    } else {

        ROS_INFO("initialized publisher with period %f [sec] / rate %f [Hz]", period, 1.0/period);
        
    }

    // define parameters
    bool timer_and_not_rate = false;
    if (timer_and_not_rate){
        
        /**
        * Timers allow you to get a callback at a specified rate.
        */
        ros::Timer timer = n.createTimer(ros::Duration(period), callback1);
        ros::spin();

    } else {
        double rate = 1.0/period;
        ros::Rate r(rate);

        while (ros::ok())
        {

        // Publish the message
        while (pub.getNumSubscribers() < 1)
        {
            if (!ros::ok())
            {
            return 0;
            }
            ROS_WARN_ONCE("Please create a subscriber to the message");
            sleep(1);
        }
        pub.publish(message);

        r.sleep();
        }
    }

    return 0;

}

