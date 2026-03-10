import rclpy
from rclpy.node import Node
import math

from geometry_msgs.msg import Twist
from turtle_interfaces.srv import SetColor
from turtle_interfaces.msg import TurtleMsg


class TurtlebotServer(Node):
    def __init__(self):
        super().__init__('turtleServer')

        # Create turtle FIRST (critical!)
        self.turtle = TurtleMsg()

        # Create service SECOND
        self.turtle_color_srv = self.create_service(
            SetColor,
            'set_color',          # valid ROS2 name
            self.set_color_callback
        )

        # Publisher of turtle state
        self.turtle_pub = self.create_publisher(TurtleMsg, 'turtleState', 1)

        # Velocities
        self.vel_x = 0
        self.ang_vel = 0

        # Subscriber for Twist commands
        self.twist_sub = self.create_subscription(
            Twist,
            'turtleDrive',
            self.twist_callback,
            1
        )

        # Driving simulation timer
        self.sim_interval = 0.02
        self.create_timer(self.sim_interval, self.driving_timer_cb)

    # -----------------------------
    # SERVICE CALLBACK
    # -----------------------------
    def set_color_callback(self, request, response):
        self.turtle.color = request.color
        self.get_logger().info(f"Turtle color set: {self.turtle.color}")
        response.ret = 1
        return response

    # -----------------------------
    # TWIST CALLBACK
    # -----------------------------
    def twist_callback(self, msg):
        self.vel_x = msg.linear.x
        self.ang_vel = msg.angular.z

    # -----------------------------
    # DRIVING SIMULATION
    # -----------------------------
    def driving_timer_cb(self):
        # Convert quaternion to yaw
        roll, pitch, yaw = rpy_from_quat(
            self.turtle.turtle_pose.orientation.x,
            self.turtle.turtle_pose.orientation.y,
            self.turtle.turtle_pose.orientation.z,
            self.turtle.turtle_pose.orientation.w
        )

        # Basic physics
        new_x = self.turtle.turtle_pose.position.x + self.vel_x * self.sim_interval * math.cos(yaw)
        new_y = self.turtle.turtle_pose.position.y + self.vel_x * self.sim_interval * math.sin(yaw)
        new_yaw = yaw + self.ang_vel * self.sim_interval

        # Assign new pose
        self.turtle.turtle_pose.position.x = new_x
        self.turtle.turtle_pose.position.y = new_y

        # Convert back to quaternion
        qx, qy, qz, qw = quat_from_rpy(0, 0, new_yaw)
        self.turtle.turtle_pose.orientation.x = qx
        self.turtle.turtle_pose.orientation.y = qy
        self.turtle.turtle_pose.orientation.z = qz
        self.turtle.turtle_pose.orientation.w = qw

        # Publish updated state
        self.turtle_pub.publish(self.turtle)


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def quat_from_rpy(roll, pitch, yaw):
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return qx, qy, qz, qw


def rpy_from_quat(x, y, z, w):
    srcp = 2 * (w * x + y * z)
    crcp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(srcp, crcp)

    sp = 2 * (w * y - z * x)
    if math.fabs(sp) >= 1:
        pitch = (sp / math.fabs(sp)) * math.pi / 2
    else:
        pitch = math.asin(sp)

    sycp = 2 * (w * z + x * y)
    cycp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(sycp, cycp)

    return roll, pitch, yaw


# -----------------------------
# MAIN
# -----------------------------
def main(args=None):
    rclpy.init(args=args)
    ser_obj = TurtlebotServer()
    ser_obj.get_logger().info('Turtlebot server started!')
    rclpy.spin(ser_obj)
    ser_obj.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
