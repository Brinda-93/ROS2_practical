#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClientNode(Node): #Modify name
    def __init__(self):
        super().__init__('add_two_ints_client_oop') # MODIFY Name
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")
        self.get_logger().info("Waiting for two ints server....")
    
    def call_add_two_ints(self, request:AddTwoInts.Request, response:AddTwoInts.Response):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Add two ints server")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = self.client_.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, request = request))
    
    def callback_call_add_two_ints(self, future, request):
        response = future.result()
        self.get_logger().info(str(request.a) + "+" + str(request.b) + "=" + str(response.sum))
    
def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = AddTwoIntsClientNode()

    node.call_add_two_ints(2, 8)
    
    rclpy.spin(node)
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()