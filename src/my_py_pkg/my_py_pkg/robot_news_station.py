#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node): #Modify name
    def __init__(self):
        super().__init__('robot_news_station') # MODIFY Name
        self.robot_name_ = "C3P0"
        self.publisher_ = self.create_publisher(String,"robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started")
    
    def publish_news(self):
        #creating the message
        msg = String()
        msg.data = "Hello Ms B from " + self.robot_name_
        self.publisher_.publish(msg)


def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = RobotNewsStationNode()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()