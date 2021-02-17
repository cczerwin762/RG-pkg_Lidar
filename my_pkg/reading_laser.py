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

	# if this doesn't work look at msg.ranges	
	def topic_callback(self, msg):
		self.get_logger().info('I heard: "%s" ' % msg.ranges[0])

def main(args = None):
	rclpy.init(args=args)

	reading_laser = ReadingLaser()
	
	rclpy.spin(reading_laser)
	# might not need following line or lines try combinations 
	# think we def need shutdown
	reading_laser.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
