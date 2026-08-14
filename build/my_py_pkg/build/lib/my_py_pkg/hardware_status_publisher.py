#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPublisherNode(Node): #Modify name
    def __init__(self):
        super().__init__('hardware_status_publisher') # MODIFY Name
        self.hw_status_pub_ = self.create_publisher(HardwareStatus, 'hardware_status', 10)
        self.timer_ = self.create_timer(1.0, self.publish_hw_status)
        self.get_logger().info('Hardware status publisher has been started')
    
    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 43.7
        msg.are_motors_ready = True
        msg.debug_message = 'Random message'
        self.hw_status_pub_.publish(msg)
        


def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = HardwareStatusPublisherNode()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()