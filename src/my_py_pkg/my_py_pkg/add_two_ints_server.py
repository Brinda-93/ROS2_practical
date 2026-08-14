#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsServiceNode(Node): #Modify name
    def __init__(self):
        super().__init__('add_two_ints_server') # MODIFY Name
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add two ints server has been started")
    
    def callback_add_two_ints(self, request:AddTwoInts.Request, response:AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response


def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = AddTwoIntsServiceNode()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()