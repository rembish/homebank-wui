#!/usr/bin/env python
try:
    from debian.changelog import Changelog
except ImportError:
    class Changelog(object):
        def __init__(self, _):
            pass

        def get_version(self):
            return '0.0.0'

from os import environ
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

here = abspath(dirname(__file__))
changelog = join(here, 'debian/changelog')
requirements = open(join(here, 'requires.txt')).readlines()
dev_requirements = open(join(here, 'dev_requires.txt')).readlines()

additional = {}

# debhelper setup FAKEROOTKEY variable
if 'FAKEROOTKEY' not in environ:
    additional['entry_points'] = {'console_scripts': [
        'homebank-cli = homebank.cli:manage'
    ]}

    requirements.extend(dev_requirements)

setup(
    name='homebank-wui',
    version=str(Changelog(open(changelog)).get_version()),
    description='Web User Interface for Homebank',
    author='Alex Rembish',
    author_email='alex@rembish.org',
    url='https://github.com/rembish/homebank-wui',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    **additional)
