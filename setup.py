from setuptools import setup
import os
from glob import glob

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cczerwin',
    maintainer_email='cczerwin@udel.edu',
    description='First Ros-Gazebo Pkg',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	    'reading_laser_node = my_pkg.reading_laser:main',
			'move_robot_node = my_pkg.move_robot:main'
        ],
    },
)
