import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from robot_interfaces.action import RobotTask


class RobotClient(Node):

    def __init__(self):

        super().__init__("robot_client")

        self.client = ActionClient(
            self,
            RobotTask,
            "robot_task"
        )

    def send_goal(self, destination):

        self.client.wait_for_server()

        goal = RobotTask.Goal()

        goal.destination = destination

        self.send_goal_future = self.client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        self.send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:

            self.get_logger().info("Goal rejected")

            return

        self.get_logger().info("Goal accepted")

        self.result_future = goal_handle.get_result_async()

        self.result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f"Progress: {feedback.progress:.0f}%"
        )

    def result_callback(self, future):

        result = future.result().result

        self.get_logger().info(result.message)


def main(args=None):

    rclpy.init(args=args)

    node = RobotClient()

    destination = input(
        "Destination (Kitchen/Home/Explore): "
    )

    node.send_goal(destination)

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()