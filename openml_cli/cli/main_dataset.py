# -*- coding: utf-8 -*-

import sys
import os
import re
import json
import hashlib
import requests
from tqdm import tqdm
from tabulate import tabulate

from openml_cli.api.API import API


def main(config, args):
    # print('config', config)
    # print('args', args)

    if 'subcmd' in args:
        api = API(config.apikey)

        # oml dataset search <term>
        if args['subcmd'] == 'search':

            if not args['json']:
                print('please wait ...')

            # Request:
            res = api.client.dataset.getAllData().response().result

            # Filter:
            headers = ('id', 'file_id', 'name', 'status')
            entries = []
            term = str(args['term']).strip().lower()
            for d in res.data.dataset:
                name = str(d.name).strip().lower()
                if term in name:
                    entry = (
                        d.did,  # id
                        d.file_id,
                        d.name,
                        d.status,
                    )
                    entries.append(entry)

            # Output:
            if args['json']:
                tbl = [dict(zip(headers, e)) for e in entries]
                print(json.dumps(tbl, indent=4, sort_keys=True))
            else:
                print(tabulate(entries, floatfmt=".0f", headers=headers))
                params = '(parameters: term={}, ({} results))'
                print(params.format(term, len(entries)))

        # oml dataset list --limit 20 --offset=30
        elif args['subcmd'] == 'list':

            # Request:
            res = api.client.dataset.getDataByLimitAndOffset(
                limit=args['limit'],
                offset=args['offset']
            ).response().result

            # Processing:
            headers = ('id', 'file_id', 'name', 'status')
            entries = []
            for d in res.data.dataset:
                entry = (
                    d.did,  # id
                    d.file_id,
                    d.name,
                    d.status,
                )
                entries.append(entry)

            # Output:
            if args['json']:
                tbl = [dict(zip(headers, e)) for e in entries]
                print(json.dumps(tbl, indent=4, sort_keys=True))
            else:
                print(tabulate(entries, floatfmt=".0f", headers=headers))
                print('(parameters: limit={}, offset={})'.format(
                    args['limit'], args['offset']))

        # oml dataset show --id 1
        elif args['subcmd'] == 'show':

            # Request:
            res = api.client.dataset.getDataSetById(
                id=args['id']
            ).response().result

            # Processing:
            entry = [
                ('id', int(res.data_set_description.id)),
                ('name', res.data_set_description.name),
                ('format', res.data_set_description.format),
                ('status', res.data_set_description.status),
                ('visibility', res.data_set_description.visibility),
                ('version', int(res.data_set_description.version)),
                ('version_label', res.data_set_description.version_label),
                ('license', res.data_set_description.licence),
                ('url', res.data_set_description.url),
                ('md5_checksum', res.data_set_description.md5_checksum),
                ('upload_date', res.data_set_description.upload_date),
                ('processing_date', res.data_set_description.processing_date),
            ]

            # Browser:
            if args['browser']:
                import webbrowser
                url = 'https://www.openml.org/d/{}'.format(
                    res.data_set_description.id)
                webbrowser.open(url)
                sys.exit(0)

            # Output:
            if args['json']:
                print(json.dumps(dict(entry), indent=4, sort_keys=True))
            else:
                print(tabulate(entry, headers=['name', 'value']))
                print('(parameter: id={})'.format(args['id']))

        # oml dataset download --id 1
        elif args['subcmd'] == 'download':

            # Request:
            res = api.client.dataset.getDataSetById(
                id=args['id']
            ).response().result

            # Processing:
            entry = [
                ('id', int(res.data_set_description.id)),
                ('name', res.data_set_description.name),
                ('format', res.data_set_description.format),
                ('status', res.data_set_description.status),
                ('visibility', res.data_set_description.visibility),
                ('version', int(res.data_set_description.version)),
                ('version_label', res.data_set_description.version_label),
                ('license', res.data_set_description.licence),
                ('url', res.data_set_description.url),
                ('md5_checksum', res.data_set_description.md5_checksum),
                ('upload_date', res.data_set_description.upload_date),
                ('processing_date', res.data_set_description.processing_date),
            ]
            entry = dict(entry)
            url = entry.get('url')

            # Request download:
            print('Downloading ... {} ... please wait.'.format(url))
            headers = {'Accept-Encoding': 'gzip'}
            res = requests.get(url, stream=True, headers=headers)

            # File size:
            file_size = None
            if 'Content-Length' in res.headers:
                file_size = int(res.headers.get('Content-Length'))

            # File name:
            filename = url.split('/')[-1]
            filename = filename.split('?')[0]

            content = res.headers.get('Content-Disposition')
            if content:
                filename = re.findall('filename=(.+)', content)
                if filename and isinstance(filename, list):
                    filename = filename[0]

            # Download:
            cwd = os.getcwd()
            filepath = os.path.join(cwd, filename)
            chunk_size = 1024
            if file_size:
                num_bars = int(file_size / chunk_size)
                with open(filepath, 'wb') as f:
                    for chunk in tqdm(res.iter_content(chunk_size=chunk_size),
                                      total=num_bars, unit='KB', desc=filepath,
                                      leave=True):
                        if chunk:
                            f.write(chunk)
            else:
                with open(filepath, 'wb') as f:
                    for chunk in res.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)

            # Compare checksums:
            checksum = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
            try:
                assert checksum == entry.get('md5_checksum')
            except AssertionError as e:
                print('Warning: The checksums are not equal.')

            print('Download completed ... {}'.format(filepath))

        sys.stdout.flush()


def _camel_to_snake(name):
    # https://stackoverflow.com/a/1176023/1293700
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
