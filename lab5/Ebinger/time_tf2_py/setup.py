from setuptools import find_packages, setup

package_name = 'time_tf2_py'

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
    maintainer='yahboom',
    maintainer_email='dreweebinger@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'turtle_tf2_broadcaster = time_tf2_py.turtle_tf2_broadcaster:main'
        'turtle_tf2_listener = time_tf2_py.turtle_tf2_listener:main'
        'fixed_frame_tf2_broadcaster = time_tf2_py.fixed_frame_tf2_broadcaster:main'
        'dynamic_frame_tf2_broadcaster = time_tf2_py.dynamic_frame_tf2_broadcaster:main'
        ],
    },
)
