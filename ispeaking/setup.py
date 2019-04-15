"""
"""
from setuptools import setup

setup(
    name='speech',
    packages=['speech'],
    include_package_data = True,
    install_requires = [
        'flask',
        ],
)
