#!/usr/bin/env python3

from setuptools import setup

setup(
    name="kyasshu_redis",
    version="0.0.1",
    description="redis backend for kyasshu",
    author="Alex Fence",
    packages=["kyasshu_redis"],
    install_requires=["redis"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta"
    ]
)
