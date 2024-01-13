#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def image_callback(msg):
    try:
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        #cv2.imwrite("/home/kazuki/fisheye.png", cv_image)
        cv2.imshow("Camera Image", cv_image)
        cv2.waitKey(1)
    except Exception as e:
        rospy.logerr(e)

def camera_visualizer_node():
    rospy.init_node("camera_visualizer_node", anonymous=True)
    rospy.Subscriber("/image/mercator", Image, image_callback)
    #rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        camera_visualizer_node()
    except rospy.ROSInterruptException:
        pass

