# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

# import six
from textwrap import dedent as textwrap_dedent


def dedent(text):
    return textwrap_dedent(text)
    # return six.b(textwrap_dedent(text))
