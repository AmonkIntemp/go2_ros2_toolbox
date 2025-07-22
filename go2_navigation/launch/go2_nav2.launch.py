from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription,DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():


    go2_navigation_path = get_package_share_directory('go2_navigation')
    map_path = os.path.join(go2_navigation_path,'maps','2-3room.yaml')
    # 设置配置文件路径
    nav2_config = os.path.join(
        go2_navigation_path,
        'config',
        'params.yaml'
    )
    print('\n\n\n\n\n\n\n\n\n')
    print(map_path)
    print(nav2_config)
    print('\n\n\n\n\n\n\n\n\n')

    # 包含nav2的launch文件
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(
                'nav2_bringup'), 'launch', 'bringup_launch.py')
        ]),
        launch_arguments={
            'map': "/home/unitree/MyWorkSpace/amonk_ros2_workspace/git_ros_project/go2_ros2_toolbox_amonk/src/go2_ros2_toolbox/go2_navigation/maps/2_3room.yaml",
            'params_file': "/home/unitree/MyWorkSpace/amonk_ros2_workspace/git_ros_project/go2_ros2_toolbox_amonk/src/go2_ros2_toolbox/go2_navigation/config/params.yaml",
            'use_sim_time': 'false',
        }.items(),
    )



    return LaunchDescription([nav2_launch])