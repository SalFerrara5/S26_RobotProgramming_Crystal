from setuptools import find_packages, setup

package_name = 'webcam'

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
    maintainer_email='lizakj@rpi.edu',
    description='Webcam publisher and subscriber package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webcam_pub = webcam.cam_pub:main',
            'webcam_sub = webcam.cam_sub:main',
        ],
    },
)

