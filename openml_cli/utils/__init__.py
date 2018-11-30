# -*- coding: utf-8 -*-

import six
from textwrap import dedent as textwrap_dedent


def dedent(text):
    return six.b(textwrap_dedent(text))
