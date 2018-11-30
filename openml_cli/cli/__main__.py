# -*- coding: utf-8 -*-

import os
import sys
from argparse import ArgumentParser, SUPPRESS, RawTextHelpFormatter, _HelpAction
from dotenv import load_dotenv, find_dotenv

from openml_cli import __version__
from openml_cli.cli import *
from openml_cli.utils import dedent


def _add_arg_help(p):
    p.add_argument(
        '-h', '--help',
        action=_HelpAction,
        help="Show this help message and exit.")


def _add_arg_version(p):
    p.add_argument(
        '-v', '--version',
        action='version',
        version='openml v{}'.format(__version__),
        help='Show the version number and exit.')


def _add_arg_debug(p):
    p.add_argument(
        '--debug',
        action='store_true',
        help=SUPPRESS)


def _configure_parser_dataset(p):
    sp = p.add_parser(
        'dataset',
        description='dataset description',
        help='dataset help',
        epilog='dataset epilog',
        add_help=False,
    )
    _add_arg_help(sp)
    sp.set_defaults(func=main_dataset.execute)


def _configure_parser_config(p):
    sp = p.add_parser(
        'config',
        description='config description',
        help='config help',
        epilog='config epilog',
        add_help=False,
    )
    _add_arg_help(sp)
    sp.set_defaults(func=main_config.execute)


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
    _add_arg_help(p)
    _add_arg_version(p)
    _add_arg_debug(p)

    # Setup subparsers:
    sp = p.add_subparsers(
        metavar='command',
        dest='cmd',
    )
    sp.required = True
    _configure_parser_dataset(sp)
    _configure_parser_config(sp)

    # Show help by default:
    if len(sys.argv) == 1:
        p.print_help(sys.stderr)
        sys.exit(1)

    return p.parse_args(args)


def parse_config():
    # https://openml.github.io/OpenML/Client-API-Standards/
    cfg_file_path = os.path.expanduser('~/.openml/config')

    # Default config:
    config = {
        'server': 'https://www.openml.org',
        'verbosity': '0'
    }

    # Write config:
    if not os.path.exists(cfg_file_path):
        os.makedirs(os.path.expanduser('~/.openml'))
        with open(cfg_file_path, 'wt') as fh:
            for key, value in config.items():
                line = '{}=[]\n'.format(key, value)
                fh.write(str(line))
        return config

    # Read config:
    with open(cfg_file_path, 'rt') as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith('#'):
                key_value = line.split('=')
                if len(key_value) == 2:
                    key = key_value[0].strip().strip('"')
                    value = key_value[1].strip().strip('"')
                    config[key] = value
    return config


def main():
    args = parse_args(sys.argv[1:])
    config = parse_config()
    if hasattr(args, 'func'):
        func = args.func
        delattr(args, 'func')
        func(config, args)


if __name__ == "__main__":
    main()
