#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node): #Modify name
    def __init__(self):
        super().__init__('number_publisher') # MODIFY Name
        self.declare_parameter("number", 2)
        self.declare_parameter("timer_period", 1.0)
        self.number_ = self.get_parameter("number").value
        self.timer_period_ = self.get_parameter("timer_period").value
        self.number_publisher_ = self.create_publisher(Int64, 'number', 10)
        self.number_timer_ = self.create_timer(1.0, self.publish_number)
        self.get_logger().info('Number publisher has been started')
    
    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)
        

def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = NumberPublisherNode()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()