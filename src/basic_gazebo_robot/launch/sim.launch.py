import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'basic_gazebo_robot'

    package_path = get_package_share_directory(package_name)

    # --------------------------------------------------
    # World
    # --------------------------------------------------

    world_file = os.path.join(
        package_path,
        'worlds',
        'my_world.world'
    )

    # --------------------------------------------------
    # Robot URDF
    # --------------------------------------------------

    robot_file = os.path.join(
        package_path,
        'urdf',
        'my_robot.urdf'
    )

    # --------------------------------------------------
    # Gazebo
    # --------------------------------------------------

    gazebo_launch_file = os.path.join(
        get_package_share_directory('gazebo_ros'),
        'launch',
        'gazebo.launch.py'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments={
            'world': world_file
        }.items()
    )

    # --------------------------------------------------
    # Read URDF
    # --------------------------------------------------

    with open(robot_file, 'r') as infp:
        robot_description = infp.read()

    # --------------------------------------------------
    # Robot State Publisher
    # --------------------------------------------------

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description
            }
        ]
    )

    # --------------------------------------------------
    # Spawn robot in Gazebo
    # --------------------------------------------------

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity',
            'my_robot',
            '-file',
            robot_file,
            '-x',
            '0.0',
            '-y',
            '0.0',
            '-z',
            '0.2'
        ],
        output='screen'
    )

    # --------------------------------------------------
    # Launch everything
    # --------------------------------------------------

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot
    ])