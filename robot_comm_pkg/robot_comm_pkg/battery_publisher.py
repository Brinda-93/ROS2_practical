import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryPublisher(Node):

    def __init__(self):

        super().__init__('battery_publisher')

        self.publisher = self.create_publisher(
            Float32,
            'battery',
            10
        )

        self.timer = self.create_timer(
            2.0,
            self.publish_data
        )

        self.level = 100.0

    def publish_data(self):

        msg = Float32()

        msg.data = self.level

        self.publisher.publish(msg)

        self.get_logger().info(
            f"Battery={msg.data:.1f}%"
        )

        self.level -= 0.5


def main(args=None):

    rclpy.init(args=args)

    node = BatteryPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()