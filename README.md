**Initial run:**

    sudo apt install ros-foxy-slam-toolbox ros-foxy-navigation2 ros-foxy-nav2-bringup

>Follow LiDAR Setup on https://github.com/Slamtec/rplidar_ros/tree/ros2-devel (Make sure to add the udev rule for the LiDAR)

<br />
<br />

**To run Perception Stack in Sim**
    
    ros2 launch autonomy autonomy_sim_launch.py


**To run Perception Stack on Robot**

    ros2 launch autonomy autonomy_launch.py

<br />
<br />


**To launch only SLAM Toolbox:**

>In Sim
    
    ros2 launch slam_toolbox online_async_launch.py params_file:=./src/autonomy/config/mapper_params_online_async.yaml use_sim_time:=true

>On Robot

    ros2 launch slam_toolbox online_async_launch.py params_file:=./src/autonomy/config/mapper_params_online_async.yaml use_sim_time:=false

<br />
<br />


**To launch only Nav2**

>In Sim

    ros2 launch nav2_bringup navigation_launch.py params_file:=./src/autonomy/config/nav2_params.yaml use_sim_time:=true

>On Robot

    ros2 launch nav2_bringup navigation_launch.py params_file:=./src/autonomy/config/nav2_params.yaml use_sim_time:=false

<br />
<br />


**To launch only the Physical LiDAR**
    
    ros2 launch rplidar_ros rplidar_a1_launch.py
