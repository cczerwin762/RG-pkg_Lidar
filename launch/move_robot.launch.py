from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	move_robot = Node(
		package = 'my_pkg',
		node_executable = 'move_robot_node',
		output = 'screen'
	)
	
	return LaunchDescription([
		move_robot
	])