#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'Jim Yong'
# __date__ = '2020/03/23'
# __contact__ = 'jimyong88@gmail.com'
# __copyright__ = 'Copyright (C) 2020, JimYong.com'

import sys

if sys.version_info < (2, 5):
    sys.exit('Python 2.5 or greater is required.')

from setuptools import setup, find_packages

VERSION = "1.0.0"

LICENSE = "MIT"

setup(
    name='idworker',
    version=VERSION,
    description=('idworker'),
    long_description="Snowflake idworker",
    author='JimYong',
    author_email='jimyong88@gmail.com',
    maintainer='JimYong',
    maintainer_email='jimyong88@gmail.com',
    license=LICENSE,
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/jimyong88/idworker',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
