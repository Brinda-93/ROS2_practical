from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class VelocityPublisher(Node):

    def __init__(self):

        super().__init__('velocity_publisher')

        self.publisher = self.create_publisher(
            Twist,
            'velocity',
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_data
        )

    def publish_data(self):

        msg = Twist()

        msg.linear.x = 1.5
        msg.angular.z = 0.2

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()