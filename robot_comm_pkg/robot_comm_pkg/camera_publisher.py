from std_msgs.msg import Int32
import rclpy
from rclpy.node import Node


class CameraPublisher(Node):

    def __init__(self):

        super().__init__('camera_publisher')

        self.publisher = self.create_publisher(
            Int32,
            'camera_fps',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_data
        )

    def publish_data(self):

        msg = Int32()

        msg.data = 30

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()