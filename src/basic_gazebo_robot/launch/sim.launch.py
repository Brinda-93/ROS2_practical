import os

from launch.actions import SetEnvironmentVariable, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'basic_gazebo_robot'

    package_path = get_package_share_directory(package_name)

    # --------------------------------------------------
    # Launch Arguments
    # --------------------------------------------------

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    slam_params_file = LaunchConfiguration(
        'slam_params_file',
        default=os.path.join(package_path, 'config', 'mapper_params_online_async.yaml')
    )

    # --------------------------------------------------
    # World
    # --------------------------------------------------

    world_file = os.path.join(
        package_path,
        'worlds',
        'small_house.world'
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
                'robot_description': robot_description,
                'use_sim_time': use_sim_time
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
    # RViz
    # --------------------------------------------------

    rviz_config_file = os.path.join(package_path, 'rviz', 'robot.rviz')

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    # --------------------------------------------------
    # SLAM Toolbox
    # --------------------------------------------------

    slam_toolbox_launch_file = os.path.join(
        get_package_share_directory('slam_toolbox'),
        'launch',
        'online_async_launch.py'
    )

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(slam_toolbox_launch_file),
        launch_arguments={
            'slam_params_file': slam_params_file,
            'use_sim_time': use_sim_time
        }.items()
    )

    # --------------------------------------------------
    # Launch everything
    # --------------------------------------------------
    gazebo_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value=os.path.join(package_path, 'models')
    )

    return LaunchDescription([
        # Arguments
        DeclareLaunchArgument('use_sim_time', default_value='true',
                              description='Use simulation clock'),
        DeclareLaunchArgument('slam_params_file',
                              default_value=os.path.join(
                                  package_path, 'config', 'mapper_params_online_async.yaml'),
                              description='Path to SLAM Toolbox params YAML'),
        # Nodes
        gazebo_model_path,
        gazebo,
        robot_state_publisher,
        spawn_robot,
        rviz,
        slam,
    ])