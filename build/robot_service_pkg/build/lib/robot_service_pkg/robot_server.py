import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger


class RobotServer(Node):

    def __init__(self):

        super().__init__('robot_server')

        self.service = self.create_service(
            Trigger,
            'move_forward',
            self.callback
        )

        self.get_logger().info("Move Forward service ready.")

    def callback(self, request, response):

        self.get_logger().info("Executing Move Forward")

        response.success = True
        response.message = "Robot moved forward."

        return response


def main(args=None):

    rclpy.init(args=args)

    node = RobotServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()