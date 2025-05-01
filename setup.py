from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ugv_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'ugv_description'), glob('ugv_description/*.xacro')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.STL')),
        (os.path.join('share', 'ugv_description', 'config'), 
     ['config/gz_bridge.yaml']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ibrahim',
    maintainer_email='Ibrahimhersi68@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={  
        'console_scripts': [
        ],
    },
)
