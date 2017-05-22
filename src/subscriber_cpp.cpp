#include "ros/ros.h"
#include <performance_tests/SuperAwesome.h>
#include <sys/time.h>

// -------------------------------
#define CLOCK_PRECISION  1E9
const int COUNTER_MAX = 6;
// -------------------------------

// -------------------------------
std::vector<double> elapsed_time(COUNTER_MAX);
int counter_ = 0;
timespec t1, t2;
// -------------------------------

double elapsedTime(const int counter){
    if (counter==0){
        // this is the first time I am called
        clock_gettime(CLOCK_REALTIME, &t1);
        return 0;

    }
    else
    {
        clock_gettime(CLOCK_REALTIME, &t2);
        double elapsed = ( t2.tv_sec - t1.tv_sec ) + ( t2.tv_nsec - t1.tv_nsec ) / CLOCK_PRECISION;
        t1 = t2;
        return elapsed;
    }
}

/**
 */
void callback(const performance_tests::SuperAwesome::ConstPtr & msg)
{
    // if there is data
    if (!msg->data.empty())
    {
        //ROS_INFO("I heard: [%s]", msg->data.c_str());

        if (counter_ < COUNTER_MAX)
        {
            elapsed_time.at(counter_) = elapsedTime(counter_);
            std::cout << elapsed_time[counter_] << std::endl;
            counter_++;
        }
        else 
        {
            counter_ = 0;
            
            std::cout << "5 times received, average: ";
            elapsed_time.assign(COUNTER_MAX,0);

        }
    }
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "subscriber_cpp");

    ros::NodeHandle n;
    
    ros::Subscriber sub_py  = n.subscribe("/test_msg_py", 1000, callback);
    ros::Subscriber sub_cpp = n.subscribe("/test_msg_cpp", 1000, callback);

    /**
     * ros::spin() will enter a loop, pumping callbacks.  With this version, all
     * callbacks will be called from within this thread (the main one).  ros::spin()
     * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
     */
    ros::spin();

    return 0;
}