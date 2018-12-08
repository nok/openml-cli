# -*- coding: utf-8 -*-

import re
import six
from textwrap import dedent as textwrap_dedent


def dedent(text):
    return str(six.u(textwrap_dedent(text)))


def camel_to_snake(text):
    # https://stackoverflow.com/a/1176023/1293700
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
