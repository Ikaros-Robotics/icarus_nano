import os
import launch

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    package_name='autonomy'
    lidar_package_name='rplidar_ros'

    slam_toolbox = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','online_async_launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    nav2 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','navigation_launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    lidar = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(lidar_package_name),'launch','rplidar_a1_launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    # Launch them all!
    return LaunchDescription([
        slam_toolbox,
        nav2,
        lidar
    ])