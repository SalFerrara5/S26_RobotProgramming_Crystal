import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool, Float32

import sys
sys.path.append('/home/pi/project_demo/lib')  # Yahboom path

try:
    from raspbot import Raspbot
except:
    print("ERROR: Could not import Raspbot library")

class ObjectDriveController(Node):

    def __init__(self):
        super().__init__('object_drive_controller')

        # === PARAMETERS ===
        self.declare_parameter('forward_speed', 80)
        self.declare_parameter('rotate_speed', 60)
        self.declare_parameter('center_tolerance', 0.1)
        self.declare_parameter('approach_distance', 0.3)

        self.forward_speed = self.get_parameter('forward_speed').value
        self.rotate_speed = self.get_parameter('rotate_speed').value
        self.center_tol = self.get_parameter('center_tolerance').value
        self.approach_dist = self.get_parameter('approach_distance').value

        # === ROBOT INIT ===
        self.bot = Raspbot()

        # === SUBSCRIBERS ===
        self.create_subscription(Bool, '/target_visible', self.visible_callback, 10)
        self.create_subscription(Float32, '/target_offset', self.offset_callback, 10)
        self.create_subscription(Float32, '/target_distance', self.distance_callback, 10)

        # === STATE ===
        self.target_visible = False
        self.target_offset = 0.0
        self.target_distance = 999.0

        # Timer loop
        self.timer = self.create_timer(0.1, self.control_loop)

        self.get_logger().info("Drive controller started")

    # === CALLBACKS ===
    def visible_callback(self, msg):
        self.target_visible = msg.data

    def offset_callback(self, msg):
        self.target_offset = msg.data

    def distance_callback(self, msg):
        self.target_distance = msg.data

    # === MOTION FUNCTIONS (from your notebooks) ===
    def move_forward(self, speed):
        self.bot.set_motor(speed, speed)

    def move_backward(self, speed):
        self.bot.set_motor(-speed, -speed)

    def rotate_left(self, speed):
        self.bot.set_motor(-speed, speed)

    def rotate_right(self, speed):
        self.bot.set_motor(speed, -speed)

    def stop_robot(self):
        self.bot.set_motor(0, 0)

    # === CONTROL LOGIC ===
    def control_loop(self):

        if not self.target_visible:
            self.get_logger().info("Searching...")
            self.rotate_left(self.rotate_speed)
            return

        # ALIGNMENT
        if abs(self.target_offset) > self.center_tol:
            if self.target_offset > 0:
                self.get_logger().info("Turning right")
                self.rotate_right(self.rotate_speed)
            else:
                self.get_logger().info("Turning left")
                self.rotate_left(self.rotate_speed)
            return

        # APPROACH
        if self.target_distance > self.approach_dist:
            self.get_logger().info("Moving forward")
            self.move_forward(self.forward_speed)
        else:
            self.get_logger().info("Target reached")
            self.stop_robot()


def main(args=None):
    rclpy.init(args=args)
    node = ObjectDriveController()
    rclpy.spin(node)

    node.stop_robot()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
