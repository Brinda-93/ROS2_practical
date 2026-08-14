#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartPhoneNode(Node): #Modify name
    def __init__(self):
        super().__init__('smartphone') # MODIFY Name
        self.subscriber_ = self.create_subscription(String, "robot_news", self.callback_robot_news, 10)
        self.get_logger().info("Smartphone has been started")

    def callback_robot_news(self, msg:String):
        self.get_logger().info(msg.data)


def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = SmartPhoneNode()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()