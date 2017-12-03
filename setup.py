#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme_file = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='duraiganbot',
    version='0.1.0',
    description='A multi-function Telegram Bot',
    long_description=readme_file,
    author='Emerson Belancieri',
    author_email='emersonbelancieri@gmail.com',
    url='https://github.com/Eihen/DuriganBot',
    license=license_file,
    packages=find_packages(exclude=('tests', 'docs'))
)
