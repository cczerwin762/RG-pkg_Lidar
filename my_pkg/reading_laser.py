import rclpy
from sensor_msgs.msg import LaserScan
from rclpy.node import Node

class ReadingLaser(Node):
	def __init__(self):
		super().__init__('reading_laser')
		defaultQoS = rclpy.qos.QoSPresetProfiles.SYSTEM_DEFAULT.value
		self.subscription = self.create_subscription(
			LaserScan,'dolly/laser_scan', self.topic_callback, defaultQoS
		)
		self.subscription
	
	def topic_callback(self, msg):
		self.get_logger().info(
		'I heard: "%s" "%d" ' % (msg.ranges[0], len(msg.ranges))
		)

def main(args = None):
	rclpy.init(args=args)
	reading_laser = ReadingLaser()
	rclpy.spin(reading_laser)
	reading_laser.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
