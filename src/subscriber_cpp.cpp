#include "ros/ros.h"
#include <performance_tests/SuperAwesome.h>
#include <sys/time.h>

#include <fstream>
#include <iterator>

// -------------------------------
#define CLOCK_PRECISION  1E9
const int COUNTER_MAX = 5000;
// -------------------------------

// -------------------------------
std::vector<double> elapsed_time(COUNTER_MAX);
int counter_ = 0;
timespec t1, t2;

bool save_to_file_= true;
std::string caller_id_ = "py";
// -------------------------------


/**
 */
void saveToFile(const std::vector<double> & data_to_save){
    std::string file_name = "subscriber_cpp_from_" + caller_id_ + "_publisher.txt";
    const char* file_name_ptr = file_name.c_str();

    std::ofstream output_file;
    output_file.open(file_name_ptr);
    for (std::vector<double>::const_iterator it = data_to_save.begin() ; it != data_to_save.end(); ++it)
        output_file << *it << "\n";
    output_file.close();

}

/**
 */
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

void measurePerformance(){
    if (counter_ < COUNTER_MAX)
    {
        elapsed_time.at(counter_) = elapsedTime(counter_);
        counter_++;
    }
    else 
    {
        counter_ = 0;

        std::cout << COUNTER_MAX << " times received messages..." << std::endl;
        if (save_to_file_) {
            saveToFile(elapsed_time);
        }

        elapsed_time.assign(COUNTER_MAX,0);

    }

}

/**
 */
void callbackPy(const performance_tests::SuperAwesome::ConstPtr & msg)
{
    // if there is data
    if (!msg->data.empty())
    {
        caller_id_ = "py";
        measurePerformance();

    }
}

/**
 */
void callbackCpp(const performance_tests::SuperAwesome::ConstPtr & msg)
{
    // if there is data
    if (!msg->data.empty())
    {
        caller_id_ = "cpp";
        measurePerformance();

    }
}


/**
 */
int main(int argc, char **argv)
{
    const char * node_name = "subscriber_cpp";
    ros::init(argc, argv, node_name);

    ros::NodeHandle n;

    ROS_INFO("Initializing %s node", node_name);

    const char * topic_py  = "/test_msg_py";
    const char * topic_cpp = "/test_msg_cpp";

    ros::Subscriber sub_py  = n.subscribe(topic_py, 1000, callbackPy);
    ros::Subscriber sub_cpp = n.subscribe(topic_cpp, 1000, callbackCpp);

    ROS_INFO("listening to two topics %s & %s", topic_py, topic_cpp);

    /**
     * ros::spin() will enter a loop, pumping callbacks.  With this version, all
     * callbacks will be called from within this thread (the main one).  ros::spin()
     * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
     */
    ros::spin();

    return 0;
}