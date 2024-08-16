im in here - Muib

test change

sudo apt install ros-foxy-slam-toolbox ros-foxy-navigation2 ros-foxy-nav2-bringup

To run in Sim you need 2 terminals:

  Terminal 1: ros2 launch slam_toolbox online_async_launch.py params_file:=./src/autonomy/config/mapper_params_online_async.yaml use_sim_time:=true

  Terminal 2: ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true

To run on Hardware you need 3 terminals:

  Terminal 1: ros2 launch slam_toolbox online_async_launch.py params_file:=./src/autonomy/config/mapper_params_online_async.yaml use_sim_time:=false

  Terminal 2: ros2 launch nav2_bringup navigation_launch.py use_sim_time:=false

  Terminal 3: sudo chmod 777 /dev/ttyUSB0 
  
  Terminal 3: ros2 launch rplidar_ros rplidar_a1_launch.py
