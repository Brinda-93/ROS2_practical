import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D

class PositionPublisher(Node): #Modify name
    def __init__(self):
        super().__init__('position_publisher') # MODIFY Node Name
        self.publisher = self.create_publisher(Pose2D,
        'robot_position', 10)

        self.timer = self.create_timer(
            1.0, self.publish_position)
        
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
    
    def publish_position(self):
        msg = Pose2D()
        msg.x = self.x
        msg.y = self.y
        msg.theta = self.theta
        self.publisher.publish(msg)

        self.get_logger().info(
            f"x={msg.x:.2f}"
            f"y={msg.y:.2f}"
            f"theta={msg.theta:.2f}"
        )

        self.x += 0.5
        self.y += 0.2
        self.theta += 5.0


def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = PositionPublisher()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)

    node.destroy_node()

    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()
