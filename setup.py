#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

req = open("requirements.txt")
requirements = req.readlines()
req.close()

# Dynamically retrieve the version information
version = __import__('iot_analytics').__version__
maintainer = __import__('iot_analytics').__maintainer__
maintainer_email = __import__('iot_analytics').__email__

setup(
    name="IOT-Analytics",
    version=version,
    url="https://github.com/gunthercox/iot-analytics",
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='readme.md',
    description="Flexable analytics for your robot or IOT device.",
    author=maintainer,
    author_email=maintainer_email,
    packages=find_packages(),
    package_dir={"iot_analytics": "iot_analytics"},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=True,
    platforms=["any"],
    keywords=["iot", "analytics"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    test_suite="tests",
    tests_require=[]
)
