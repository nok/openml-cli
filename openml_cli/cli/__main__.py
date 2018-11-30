# -*- coding: utf-8 -*-

import os
import sys
from argparse import ArgumentParser, SUPPRESS, RawTextHelpFormatter, _HelpAction

from openml_cli import __version__
from openml_cli.cli import *
from openml_cli.api.Config import Config
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
        version='{}'.format(__version__),
        help='Show the version number and exit.')


def _add_arg_debug(p):
    p.add_argument(
        '--debug',
        action='store_true',
        help=SUPPRESS)


def _configure_parser_dataset(p):
    """Configure `datasets` subparser"""
    sp = p.add_parser(
        'dataset',
        description='dataset description',
        help='Search or download datasets.',
        epilog='dataset epilog',
        add_help=False,
    )
    _add_arg_help(sp)
    sp.set_defaults(func=main_dataset.main)


def _configure_parser_config(p):
    """Configure `config` subparser"""

    # command `config`
    config_p = p.add_parser(
        'config',
        description='List and change the configuration.',
        help='List and change the configuration.',
        add_help=False,
    )
    sub = config_p.add_subparsers(
        metavar='subcommand',
        dest='subcmd',
    )
    sub.required = True

    # subcommand `config view`
    config_view_p = sub.add_parser(
        'view',
        description='dataset description',
        help='Print all configuration parameters.',
        add_help=False,
    )
    config_view_p.set_defaults(func=main_config.main)

    # subcommand `config set --name NAME --value VALUE`
    config_set_p = sub.add_parser(
        'set',
        description='Change the configuration.',
        help='Change a configuration parameter.',
        add_help=False,
    )
    config_set_p.set_defaults(func=main_config.main)
    config_set_p.add_argument(
        '--name', '-n',
        choices=Config.DEFAULT_PARAMS.keys(),
        required=True,
        help='Set the key of the parameter.'
    )
    config_set_p.add_argument(
        '--value', '-v',
        required=True,
        help='Set the value of the parameter.'
    )
    _add_arg_help(config_set_p)

    # subcommand `config unset --name NAME`
    config_unset_p = sub.add_parser(
        'unset',
        description='Revert the configuration.',
        help='Revert a configuration parameter.',
        # epilog='',
        add_help=False,
    )
    config_unset_p.set_defaults(func=main_config.main)
    config_unset_p.add_argument(
        '--name', '-n',
        choices=Config.DEFAULT_PARAMS.keys(),
        required=True,
        help='Set the key of the parameter.'
    )
    _add_arg_help(config_unset_p)

    _add_arg_help(config_p)
    if len(sys.argv) == 2 and sys.argv[1] == 'config':
        config_p.print_help(sys.stdout)
        sys.exit(1)


def parse_args(args):
    """Load and parse applied arguments"""

    description = dedent("""
        OpenML CLI v{}
          https://github.com/nok/openml-cli
          https://www.openml.org/
    """).format(__version__)

    epilog = dedent("""
        examples:
          `oml config view`
          `oml config set apikey YOUR_APIKEY`
    """).format(__version__)

    p = ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=RawTextHelpFormatter,
        add_help=False)
    _add_arg_help(p)
    _add_arg_version(p)
    _add_arg_debug(p)

    sp = p.add_subparsers(
        metavar='command',
        dest='cmd',
    )
    sp.required = True
    _configure_parser_dataset(sp)
    _configure_parser_config(sp)

    if len(sys.argv) == 1:
        p.print_help(sys.stdout)
        sys.exit(1)

    return p.parse_args(args)


def parse_env():
    """Load and parse .env file"""
    env_file = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.exists(env_file):
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=env_file, override=True)


def main():
    config = Config('~/.openml/config')
    args = parse_args(sys.argv[1:])

    if hasattr(args, 'func'):
        func = args.func
        delattr(args, 'func')
        func(config, vars(args))


if __name__ == "__main__":
    main()
