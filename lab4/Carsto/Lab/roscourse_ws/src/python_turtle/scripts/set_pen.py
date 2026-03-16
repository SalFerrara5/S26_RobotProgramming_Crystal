import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen

def main():
    rclpy.init()
    node = Node('set_pen_client')

    client = node.create_client(SetPen, '/turtle1/set_pen')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('Waiting for /turtle1/set_pen service...')

    req = SetPen.Request()
    req.r = 255
    req.g = 0
    req.b = 0
    req.width = 3
    req.off = 0
    
    client = node.create_client(SetPen, '/turtle2/set_pen')
    req.r = 0
    req.g = 0
    req.b = 255
    req.width = 3
    req.off = 0

    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    node.get_logger().info(f'Result: {future.result()}')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
