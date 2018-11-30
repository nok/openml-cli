# -*- coding: utf-8 -*-


def main(config, args):
    if 'subcmd' in args:

        # oml config view
        if args['subcmd'] == 'view':
            config.list()

        # oml config set --name <NAME> --value <VALUE>
        elif args['subcmd'] == 'set':
            config.set(args['name'], args['value'])

        # oml config unset --name <NAME>
        elif args['subcmd'] == 'unset':
            config.unset(args['name'])
