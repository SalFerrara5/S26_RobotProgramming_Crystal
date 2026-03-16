import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from turtle_interfaces.action import MakeSquare
from rcl_interfaces.msg import ParameterDescriptor


class TurtleActionClient(Node):

    def __init__(self):
        super().__init__('turtle_action_client')

        self.declare_parameter(
            'square_size',
            100.0,
            ParameterDescriptor(description='Size of the square')
        )

        self._action_client = ActionClient(self, MakeSquare, 'make_square')


    def send_goal(self):

        goal_msg = MakeSquare.Goal()

        goal_msg.square_size = self.get_parameter(
            'square_size').get_parameter_value().double_value

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)


    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)


    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback
        self.get_logger().info(
            f'Heading: {feedback.current_pose.heading}, Position: {feedback.current_pose.position}'
        )


    def get_result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f'Final pose: heading {result.final_pose.heading}, position {result.final_pose.position}'
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    action_client = TurtleActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
