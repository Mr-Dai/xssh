#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import setup


setup(
    name="xssh",
    version="0.1.0",
    description="Easy SSH tool for server administrators",
    author="Robert Peng",
    author_email="robert.peng@foxmail.com",
    url="https://github.com/Mr-Dai/xssh",
    packages=["xssh"],
    install_requires=[
        "six>=1.12.0",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
)
