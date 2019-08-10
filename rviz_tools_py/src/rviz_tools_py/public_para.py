#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geometry_msgs.msg import Vector3

class Public_para():
    
    # parameters for static node: map elemetents
    '''
    TODO : 
    1. ADD the traffic light and lane_markers
    2. discrimenate different type of lanes
    '''
    package_name = 'rviz_tools_py'
    static_pub_rate = 10
    wait_time = None
    static_node_name = 'static_marker'
    static_frame = '/map'
    static_divider_topic = 'markers_divider'
    one_scence = '/home/apple/catkin_ws/src/rviz_tools_py/data/gps_pre_frame2.npy'
    divider_txt = '/home/apple/catkin_ws/src/rviz_tools_py/data/divider_hdmap.txt'
    divider_color = 'white'
    divider_ArrayTopic = 'path_Array'
    static_refresh_time = 1.2
    divider_width = 0.1

    '''
    parameters for dynamic node, elements indlude:
    point cloud, car model, trajector GPS and TF transformation
    TODO :
    1. solve the synchronization the problem in ROS system
    2. add the WASD control to change the view
    3. set the default view window via code
    4. Add beautiful 3D model into Rviz and build the enviroments
    '''
    np_data_path = '/home/apple/catkin_ws/src/rviz_tools_py/data/gps_pre_frame2.npy'
    dynamic_node_name = 'dynamic_marker'
    car_arrow_topic = 'car_and_heading'
    dynamic_base_frame = '/vehicle'
    dynamic_single_marker_topic = 'single_topic'
    point_cloud_topic = 'point_cloud'
    arrow_color = 'blue'
    car_stl_model = "package://rviz_tools_py/meshes/car_stl.stl"
    car_color = None
    dynamic_pub_rate = 40
    dynamic_refresh_time = 1/dynamic_pub_rate
    dynamic_refresh_time_slow = dynamic_refresh_time/10

    # scale is for arrow
    scale = Vector3(1.0,0.2,0.2) # x=length, y=height, z=height
    # mesh_scale is for car model
    mesh_scale = 0.3