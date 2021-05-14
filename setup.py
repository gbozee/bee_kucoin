#!/usr/bin/env python
import codecs
import os
import re
import sys
from setuptools import setup,find_packages

here = os.path.abspath(os.path.dirname(__file__))



def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def install_requires():

    requires = ['kucoin-futures-python==1.0.3','kucoin-python==1.0.7']
    return requires


setup(
    name='bee_kucoin',
    version="0.0.1",
    packages=find_packages(),
    description='Kucoin REST API v2 python implementation',
    url='https://github.com/sammchardy/python-kucoin',
    author='Sam McHardy',
    license='MIT',
    author_email='',
    install_requires=install_requires(),
    keywords='kucoin exchange rest api bitcoin ethereum btc eth kcs',
    classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
