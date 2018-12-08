# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages


def read_version():
    """Read the module version from __version__.txt"""
    src_dir = os.path.abspath(os.path.dirname(__file__))
    ver_file = os.path.join(src_dir, 'openml_cli', '__version__.txt')
    version = open(ver_file, 'r').readlines().pop()
    if isinstance(version, bytes):
        version = version.decode('utf-8')
    version = str(version).strip()
    return version


def parse_requirements():
    """Parse the modules from requirements.txt"""
    src_dir = os.path.abspath(os.path.dirname(__file__))
    req_file = os.path.join(src_dir, 'requirements.txt')
    reqs = open(req_file, 'r').read().strip().split('\n')
    reqs = [req.strip() for req in reqs if 'git+' not in req]
    return reqs


setup(
    name='openml-cli',
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    version=read_version(),
    description='Use the command line tool `oml` or `openml` '
                'to interact with the official API of OpenML.',
    author='Darius Morawiec',
    author_email='mail@nok.onl',
    url='https://github.com/nok/openml-cli',
    entry_points={
        'console_scripts': [
            'openml = openml_cli.cli.__main__:main',
            'oml = openml_cli.cli.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=parse_requirements(),
    keywords=['openml', 'openscience', 'cli', 'datasets'],
    license='MIT',
)
