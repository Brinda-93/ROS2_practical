from std_msgs.msg import Float32
import rclpy
from rclpy.node import Node


class TemperaturePublisher(Node):

    def __init__(self):

        super().__init__('temperature_publisher')

        self.publisher = self.create_publisher(
            Float32,
            'temperature',
            10
        )

        self.timer = self.create_timer(
            3.0,
            self.publish_data
        )

        self.temp = 28.0

    def publish_data(self):

        msg = Float32()

        msg.data = self.temp

        self.publisher.publish(msg)

        self.temp += 0.1


def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()