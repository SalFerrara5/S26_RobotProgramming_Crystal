import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32

import sys
import os

possible_paths = [
    '/home/pi/project_demo/lib',
    '/home/yahboom/project_demo/lib',
]

for path in possible_paths:
    if os.path.exists(path):
        sys.path.append(path)

try:
    from McLumk_Wheel_Sports import *
except Exception as e:
    raise RuntimeError(f"Could not import McLumk_Wheel_Sports: {e}")


class ObjectDriveController(Node):

    def __init__(self):
        super().__init__('object_drive_controller')

        self.declare_parameter('forward_speed', 80)
        self.declare_parameter('rotate_speed', 60)
        self.declare_parameter('center_tolerance', 0.1)
        self.declare_parameter('approach_distance', 0.3)

        self.forward_speed = self.get_parameter('forward_speed').value
        self.rotate_speed = self.get_parameter('rotate_speed').value
        self.center_tol = self.get_parameter('center_tolerance').value
        self.approach_dist = self.get_parameter('approach_distance').value

        self.create_subscription(Bool, '/target_visible', self.visible_callback, 10)
        self.create_subscription(Float32, '/target_offset', self.offset_callback, 10)
        self.create_subscription(Float32, '/target_distance', self.distance_callback, 10)

        self.target_visible = False
        self.target_offset = 0.0
        self.target_distance = 999.0

        self.timer = self.create_timer(0.1, self.control_loop)

        self.get_logger().info("Drive controller started")

    def visible_callback(self, msg):
        self.target_visible = msg.data

    def offset_callback(self, msg):
        self.target_offset = msg.data

    def distance_callback(self, msg):
        self.target_distance = msg.data

    def control_loop(self):
        if not self.target_visible:
            self.get_logger().info("Searching...")
            rotate_left(self.rotate_speed)
            return

        if abs(self.target_offset) > self.center_tol:
            if self.target_offset > 0:
                self.get_logger().info("Turning right")
                rotate_right(self.rotate_speed)
            else:
                self.get_logger().info("Turning left")
                rotate_left(self.rotate_speed)
            return

        if self.target_distance > self.approach_dist:
            self.get_logger().info("Moving forward")
            move_forward(self.forward_speed)
        else:
            self.get_logger().info("Target reached")
            stop_robot()


def main(args=None):
    rclpy.init(args=args)
    node = ObjectDriveController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    stop_robot()
    node.destroy_node()
    rclpy.shutdown()

    try:
        del bot
    except:
        pass


if __name__ == '__main__':
    main()
