#!/usr/bin/env python

from setuptools import setup, find_packages
readme = open('README.md').read()
setup(name='pyharmony',
      version='1.0',
      description='Python API for Logitech Harmony Hub',
      author='Jeff Terrace',
      author_email='jterrace@gmail.com',
      url='http://www.github.com/zonyl/pyharmony',
      packages=find_packages())
