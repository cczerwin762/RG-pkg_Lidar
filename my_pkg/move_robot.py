import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node

class MinimalPublisher(Node):
	def __init__(self):
		super().__init__('minimal_publisher')
		self.publisher_= self.create_publisher(
			Twist, '/dolly/cmd_vel', 10
		)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0
		
	def timer_callback(self):
		msg = Twist()
		msg.linear.x = 0.5
		self.publisher_.publish(msg)
		self.i +=1
		
def main(args = None):
	rclpy.init(args=args)
	minimal_publisher = MinimalPublisher()
	rclpy.spin(minimal_publisher)
	minimal_publisher.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()