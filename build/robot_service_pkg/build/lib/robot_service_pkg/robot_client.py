import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger


class RobotClient(Node):

    def __init__(self):

        super().__init__('robot_client')

        self.client = self.create_client(
            Trigger,
            'move_forward'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")

    def send_request(self):

        request = Trigger.Request()

        future = self.client.call_async(request)

        rclpy.spin_until_future_complete(self, future)

        return future.result()


def main(args=None):

    rclpy.init(args=args)

    node = RobotClient()

    result = node.send_request()

    node.get_logger().info(
        f"{result.success} : {result.message}"
    )

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()