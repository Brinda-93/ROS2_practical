from setuptools import find_packages, setup

package_name = 'robot_comm_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bs5',
    maintainer_email='frizzyhair123456789@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'position_pub = robot_comm_pkg.position_publisher:main',

        'position_sub = robot_comm_pkg.position_subscriber:main',
        'battery_pub = robot_comm_pkg.battery_publisher:main',

        'velocity_pub = robot_comm_pkg.velocity_publisher:main',

        'temperature_pub = robot_comm_pkg.temperature_publisher:main',

        'camera_pub = robot_comm_pkg.camera_publisher:main',
        ],
    },
)
