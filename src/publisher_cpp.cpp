
#include <ros/ros.h>
#include <performance_tests/SuperAwesome.h>


int main( int argc, char** argv )
{
    // initialize the node and define handle
    ros::init(argc, argv, "publisher_cpp");
    ros::NodeHandle n;

    // define parameters
    double rate;
    n.getParam("rate",rate);

    // check if block_position_z_ is given
    if ( !n.getParam("rate",rate)){
        rate = 5;
        ROS_INFO("setting rate to 5Hz");
    }
    
    // set the rate to 5Hz
    ros::Rate r(rate);

    // define the publisher
    ros::Publisher marker_pub = 
        n.advertise<performance_tests::SuperAwesome>("test_msg_cpp", 1);


    performance_tests::SuperAwesome marker;
    
    marker.data = "string_message";

    // Set the scale of the marker -- 1x1x1 here means 1m on a side
    // position of our cube with respect to the given frame
    while (ros::ok())
    {
        // Set the pose of the marker.  This is a full 6DOF pose relative to the frame/time specified in the header
        //marker.points.push_back(tmp_p);

        // Publish the marker
        while (marker_pub.getNumSubscribers() < 1)
        {
          if (!ros::ok())
          {
            return 0;
          }
          ROS_WARN_ONCE("Please create a subscriber to the marker");
          sleep(1);
        }

        marker.stamp = ros::Time::now();
        marker_pub.publish(marker);

        r.sleep();
    }

}

