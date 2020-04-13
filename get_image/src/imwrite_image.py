import numpy as np
from sensor_msgs.msg import CompressedImage
import rospy
import cv2
import datetime
import os

count = 0
year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day
minute = datetime.datetime.today().minute
hour = datetime.datetime.today().hour

def image_callback(ros_data):
    global count
    np_arr = np.fromstring(ros_data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    # cv2.imshow('cv_img', image_np)
    # cv2.waitKey(2)

    path = "./image/" + str(year) + "_" + str(month) + "_" + str(day) + "_" + str(hour) + "_" + str(minute) + "/"
    if not(os.path.isdir(path)):
        os.makedirs(os.path.join(path))

    if count % 1 == 0:
        cv2.imwrite(path + str(count) + ".jpg", image_np)
    count += 1

def main():
    rospy.init_node('imwrite_image', anonymous = True)
    rospy.Subscriber("/uav/camera/left/image_rect_color/compressed", CompressedImage, image_callback, queue_size=1)
    rospy.spin()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass