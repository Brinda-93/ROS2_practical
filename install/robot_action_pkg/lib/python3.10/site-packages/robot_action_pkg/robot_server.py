import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from robot_interfaces.action import RobotTask


class RobotServer(Node):

    def __init__(self):

        super().__init__("robot_server")

        self.server = ActionServer(
            self,
            RobotTask,
            "robot_task",
            self.execute_callback
        )

    def execute_callback(self, goal_handle):

        self.get_logger().info(
            f"Destination: {goal_handle.request.destination}"
        )

        feedback = RobotTask.Feedback()

        for i in range(101):

            if goal_handle.is_cancel_requested:

                goal_handle.canceled()

                result = RobotTask.Result()

                result.success = False
                result.message = "Task Cancelled"

                return result

            feedback.progress = float(i)

            goal_handle.publish_feedback(feedback)

            time.sleep(0.1)

        goal_handle.succeed()

        result = RobotTask.Result()

        result.success = True

        result.message = (
            f"Reached {goal_handle.request.destination}"
        )

        return result


def main(args=None):

    rclpy.init(args=args)

    node = RobotServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()