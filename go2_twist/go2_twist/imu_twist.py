import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class IMURemapNode(Node):
    def __init__(self):
        super().__init__('imu_twist')

        self.subscription = self.create_subscription(
            Imu,
            '/utlidar/imu',
            self.imu_callback,
            100  # Hz
        )

        self.publisher = self.create_publisher(
            Imu,
            '/imu',
            10
        )

    def imu_callback(self, msg):
        msg.header.frame_id = 'base_link'
        msg.header.stamp = self.get_clock().now().to_msg()
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = IMURemapNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
