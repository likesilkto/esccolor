#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import sys
sys.path.append('./tests')

setup(
	name= 'esccolor', # Application name:
	version= '0.0.1', # Version number

	author= 'Masayuki Tanaka', # Author name
	author_email= 'm@like.silk.to', # Author mail	

	url='https://github.com/likesilkto/esccolor', # Details
	description='Colorize text for console print.', # short description
	long_description='Colorize text for console print.', # long description
	install_requires=[ # Dependent packages (distributions)
	],
	
	include_package_data=False, # Include additional files into the package
	packages=find_packages(),

	test_suite = 'tests',

	classifiers=[
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: MIT',
    ]
)

# python -m unittest tests.test_

# uninstall
# % python setup.py install --record installed_files
# % cat installed_files | xargs rm -rf
# % rm installed_files

