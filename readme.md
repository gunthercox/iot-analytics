# IOT Analytics

**Analytics for your robot or IOT device**

[![Package Version](https://img.shields.io/pypi/v/iot-analytics.svg)](https://pypi.python.org/pypi/iot-analytics/)
[![Build Status](https://travis-ci.org/gunthercox/iot-analytics.svg?branch=master)](https://travis-ci.org/gunthercox/iot-analytics)
[![Coverage Status](https://coveralls.io/repos/gunthercox/iot-analytics/badge.svg?branch=master&service=github)](https://coveralls.io/github/gunthercox/iot-analytics?branch=master)

This is a python module designed to provide the tools and resources needed to gather analytics for real-world objects and events. Analytics for online sites and services make it possible for developers to improve workflows and optimize the performance of web pages. The same techniques can be applied to tangible objects and events.

There are many examples of programmers using services such as [Google Analytics](https://analytics.google.com) to track everything from doors opening in a home to trips to the store. Check out this [this great blog post](http://nicomiceli.com/tracking-your-home-with-google-analytics/) by Nico Miceli for an example.

## Installation

```
pip install iot_analytics
```

# Project design
This module has two main components

1. Recording data
2. Data analysis

![Program structure](https://docs.google.com/drawings/d/1YADVW9SALABGYiPmshEoD1b-sU6GFY7G6O4L7ce9eMo/pub?w=960&amp;h=720)

# Recording data

**Supported Endpoints**

- [Google Analytics](https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide)
- IOT Analytics - A custom solution built into this project that you can host your self

# Data analysis

Analytics is the discovery and communication of meaningful patterns in data. It is not possible for humans to easily extract meaning from a collection of billions of database entries. The goal of the data analysis portion of this project is to provide tools that make it easier to view and process data in a way that makes data features and trends more apparent.

# Apps

This project includes an `apps` module which adds support for integration
with the [Zorg](https://github.com/zorg/zorg) robotics framework.

# Roadmap
- Add data analysis features for hosted storage
- Integration with [Phant](https://data.sparkfun.com)
- Integration with [Intel IOT Analytics](https://dashboard.us.enableiot.com)
