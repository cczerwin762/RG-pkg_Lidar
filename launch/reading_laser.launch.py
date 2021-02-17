from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	reading_laser = Node(
		package = 'my_pkg',
		node_executable = 'reading_laser_node',
		output = 'screen',
		remappings = [
			('dolly/laser_scan', '/dolly/laser_scan')
		]
	)
	
	return LaunchDescription([
		reading_laser
	])

