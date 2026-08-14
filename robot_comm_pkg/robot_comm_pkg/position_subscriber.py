import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D

class PositionSubscriber(Node): #Modify name
    def __init__(self):
        super().__init__('position_subscriber') # MODIFY Name

        self.subscription = self.create_subscription(Pose2D, 'robot_position',
            self.callback, 10)
    
    def callback(self, msg):
        self.get_logger().info(
            f"Received "
            f"x={msg.x:.2f} "
            f"y={msg.y:.2f} "
            f"theta={msg.theta:.2f} "
        )



def main(args = None):
    # Initializing ROS2
    rclpy.init(args = args)

    # Node initilization
    node = PositionSubscriber()

    # To keep the node alive without shutdown until CTRL+C
    rclpy.spin(node)

    rclpy.destroy_node()
    
    # Last line to be run
    rclpy.shutdown()

if __name__ == '__main__':
    main()
