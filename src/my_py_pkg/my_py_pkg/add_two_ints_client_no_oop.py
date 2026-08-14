#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = Node("add_two_ints_client_no_oop")

    client = node.create_client(AddTwoInts, "add_two_ints")
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for Add two ints server")

    request = AddTwoInts.Request()
    request.a = 3
    request.b = 8
    future = client.call_async(request)
    # spin the node until there is a response
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node.get_logger().info(str(request.a) + "+" + str(request.b) + "=" + str(response.sum))
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()