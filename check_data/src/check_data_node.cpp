#include <stdio.h>
#include <ros/ros.h>
#include <time.h>

#include <std_msgs/Float64.h>

using namespace std;

std_msgs::Float64 input_data;

double cur_time_secs;
uint64_t cur_time_nsecs;
double real_cur_time;

ros::Time cur_time;

void final_data_callback(const std_msgs::Float64::ConstPtr& msg)
{
    input_data = *msg;

    cur_time = ros::Time::now();
    cur_time_secs = cur_time.sec;
    cur_time_nsecs = cur_time.nsec;
    real_cur_time = cur_time_secs + (cur_time_nsecs * 0.000000001);

    printf("latency %f\n", real_cur_time - input_data.data);    
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "get_final_data");
    ros::NodeHandle nh_sub;
    
    ros::Subscriber final_data_sub = nh_sub.subscribe("/final_data", 1, final_data_callback);
    ros::spin();
}