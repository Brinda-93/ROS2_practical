import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/data2/Brinda/Documents/Reports/ROS2/my_ros2_workspace/install/robot_action_pkg'
