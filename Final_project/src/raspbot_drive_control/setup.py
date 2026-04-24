from setuptools import setup

package_name = 'raspbot_drive_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lizakj',
    maintainer_email='lizakj@rpi.edu',
    description='Driving control node for Raspbot V2',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'object_drive_controller = raspbot_drive_control.object_drive_controller:main',
            'motor_test = raspbot_drive_control.motor_test:main',
        ],
    },
)
