import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

		pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
		pkg_dolly_gazebo = get_package_share_directory('dolly_gazebo')

		# Gazebo launch
		gazebo = IncludeLaunchDescription(
				PythonLaunchDescriptionSource(
						os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
				)
		)
		
		reading_laser = Node(
			package = 'my_pkg',
			node_executable = 'reading_laser_node',
			output = 'screen',
			remappings = [
				('dolly/laser_scan', '/dolly/laser_scan')
			]
		)

		return LaunchDescription([
				DeclareLaunchArgument(
					'world',
					default_value=[os.path.join(pkg_dolly_gazebo, 'worlds', 'dolly_empty.world'), ''],
					description='SDF world file'),
				gazebo,
				reading_laser
		])


