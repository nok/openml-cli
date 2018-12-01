# -*- coding: utf-8 -*-

import sys
import re
from tabulate import tabulate
from openml_cli.api.API import API


def main(config, args):
    # print('config', config)
    # print('args', args)

    if 'subcmd' in args:
        api = API(config.apikey)

        # oml dataset list --limit 20 --offset=30
        if args['subcmd'] == 'list':
            res = api.client.dataset.getDataByLimitAndOffset(
                limit=args['limit'],
                offset=args['offset']
            ).response().result
            tbl = []
            headers = ('id', 'file_id', 'name', 'number_of_classes',
                       'number_of_features', 'number_of_instances')
            for d in res.data.dataset:
                qualities = ()
                for idx, quality in enumerate(sorted(d.quality)):
                    qualities += ((_camel_to_snake(quality.name), quality.value), )
                qualities = dict(qualities)
                values = (d.did, d.file_id, d.name,
                          qualities['number_of_classes'],
                          qualities['number_of_features'],
                          qualities['number_of_instances'])
                tbl.append(values)
            print(tabulate(tbl, headers=headers))
            print('(parameters: limit={}, offset={})'.format(
                args['limit'], args['offset']))

        # oml dataset show --id 1
        elif args['subcmd'] == 'show':
            res = api.client.dataset.getDataSetById(
                id=args['id']
            ).response().result
            tbl = [
                ('id', res.data_set_description.id),
                ('name', res.data_set_description.name),
                ('format', res.data_set_description.format),
                ('status', res.data_set_description.status),
                ('visibility', res.data_set_description.visibility),
                ('version', res.data_set_description.version),
                ('version_label', res.data_set_description.version_label),
                ('license', res.data_set_description.licence),
                ('url', res.data_set_description.url),
                ('md5_checksum', res.data_set_description.md5_checksum),
                ('upload_date', res.data_set_description.upload_date),
                ('processing_date', res.data_set_description.processing_date),
            ]
            print(tabulate(tbl, headers=['name', 'value']))
            print('(parameter: id={})'.format(args['id']))

        sys.stdout.flush()


def _camel_to_snake(name):
    # https://stackoverflow.com/a/1176023/1293700
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
