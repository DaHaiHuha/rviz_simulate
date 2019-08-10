#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python includeswhich
import numpy as np
import random

# ROS includes
import roslib
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, Polygon
from tf import transformations  # rotation_matrix(), concatenate_matrices()

import rviz_tools_py.readpb as readpb
import rviz_tools_py.rviz_tools as rviz_tools

# import and define the public_parameter
from rviz_tools_py.public_para import Public_para as _para

# Initialize the ROS Node
rospy.init_node(_para.static_node_name, anonymous=False,
                log_level=rospy.INFO, disable_signals=False)

rate = rospy.Rate(_para.static_pub_rate)
divider_color = _para.divider_color

# initialize the publish class
markers_divider = rviz_tools.RvizMarkers(
    _para.static_frame, _para.static_divider_topic)

# path and load data
points = readpb.read_divider_txt(
    file_path=_para.divider_txt)


while not rospy.is_shutdown():
    rviz_tools.genPublishPathArray_simple(
        points, markers_divider, divider_color, _para.divider_width, lifetime=_para.static_refresh_time, toArray=True)
    rate.sleep()  # 1 Hz

# markers.publishPath(
#    paths, colors, width, pathArray.in_id, lifetime, toArray)
# paths = a list of points

# import sys
# sys.path.append("..")
# import hd_map.readpb as readpb
# # print(points)
# markers_gps = rviz_tools.RvizMarkers('/map', 'markers_gps')
# local_point, headings = readpb.read_gps_all(path = '/home/apple/catkin_ws/src/rviz_tools_py/data')
# gps_test_path = '/home/apple/catkin_ws/src/rviz_tools_py/data/GPStrafficLine.txt'
# markers_divider = rviz_tools.RvizMarkers('/map', 'markers_divider')
# #message = readpb.read_from_pb_debug()
# #points = readpb.read_divider(message)
