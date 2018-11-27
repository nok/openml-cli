# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os
import os.path


def _read_version():
    """Read the module version from __version__.txt"""
    source_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(source_dir, '__version__.txt')
    version = open(version_file, 'r').readlines().pop()
    if isinstance(version, bytes):
        version = version.decode('utf-8')
    version = str(version).strip()
    return version


__version__ = _read_version()
