# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import sys
# import os
# from os.path import abspath, expanduser, join
from argparse import ArgumentParser, SUPPRESS, RawTextHelpFormatter, _HelpAction

from . import *
from .. import __version__
from ..utils import dedent


def add_arg_help(p):
    p.add_argument(
        '-h', '--help',
        action=_HelpAction,
        help="Show this help message and exit.")


def add_arg_version(p):
    p.add_argument(
        '-v', '--version',
        action='version',
        version='openml v{}'.format(__version__),
        help='Show the version number and exit.')


def add_arg_debug(p):
    p.add_argument(
        '--debug',
        action='store_true',
        help=SUPPRESS)


def parse_args(args):
    description = dedent("""
        OpenML CLI
    """)
    epilog = 'More details on https://github.com/nok/openml-cli'

    # Setup parser:
    p = ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=RawTextHelpFormatter,
        add_help=False)
    add_arg_help(p)
    add_arg_version(p)
    add_arg_debug(p)

    # Setup subparsers:
    sp = p.add_subparsers(
        metavar='command',
        dest='cmd',
    )
    sp.required = True
    configure_parser_dataset(sp)
    configure_parser_config(sp)

    # Show help by default:
    if len(sys.argv) == 1:
        p.print_help(sys.stderr)
        sys.exit(1)

    # Call the subparser:
    args = p.parse_args(args)
    func = args.func
    delattr(args, 'func')
    func(args)


def configure_parser_dataset(p):
    sp = p.add_parser(
        'dataset',
        description='dataset description',
        help='dataset help',
        epilog='dataset epilog',
        add_help=False,
    )
    add_arg_help(sp)
    sp.set_defaults(func=main_dataset.execute)


def configure_parser_config(p):
    sp = p.add_parser(
        'config',
        description='config description',
        help='config help',
        epilog='config epilog',
        add_help=False,
    )
    add_arg_help(sp)
    sp.set_defaults(func=main_config.execute)


def main():
    parse_args(sys.argv[1:])


if __name__ == "__main__":
    main()
