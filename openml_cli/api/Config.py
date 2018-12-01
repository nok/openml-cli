# -*- coding: utf-8 -*-

import os
import sys
from tabulate import tabulate


class Config:

    DEFAULT_PARAMS = {
        'apikey': '',
        'server': 'https://www.openml.org',
        'verbosity': '0'
    }

    def __init__(self, path='~/.openml/config'):
        self.path = str(os.path.expanduser(path))
        if not os.path.exists(self.path):
            self.config = Config.init(self.path)
        else:
            self.config = Config.load(self.path)

    def __getitem__(self, item):
        return self.config.get(item)

    @property
    def server(self):
        if 'server' in self.config.keys():
            server = self.config.get('server')
            if server != '':
                return server
        return None

    @property
    def apikey(self):
        if 'apikey' in self.config.keys():
            apikey = self.config.get('apikey')
            if apikey != '':
                return apikey
        return None

    @staticmethod
    def init(path):
        dir_ = os.path.dirname(path)
        if not os.path.exists(dir_):
            try:
                os.makedirs(dir_)
            except OSError as e:
                pass
        return Config.save(Config.DEFAULT_PARAMS)

    @staticmethod
    def save(path, config):
        flag = os.O_WRONLY | os.O_CREAT
        with os.fdopen(os.open(path, flag, 0o600), 'wt') as fh:
            fh.truncate(0)
            for key, val in sorted(config.items()):
                line = '{}={}\n'.format(key, val)
                fh.write(str(line))
        return config

    @staticmethod
    def load(path):
        config = {}
        with open(path, 'rt') as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith('#'):
                    key_vals = line.split('=')
                    if len(key_vals) > 1:
                        key = str(key_vals[0]).strip().strip('"')
                        val = '='.join(key_vals[1:])
                        val = val.strip().strip('"')
                        config[key] = val
        return config

    def set(self, key, val):
        val = str(val).strip().strip('"')
        if key in Config.DEFAULT_PARAMS.keys() and len(val) > 0:
            self.config[key] = val
            Config.save(self.path, self.config)

    def unset(self, key):
        if key in Config.DEFAULT_PARAMS.keys():
            self.config[key] = Config.DEFAULT_PARAMS.get(key)
            Config.save(self.path, self.config)

    def list(self):
        print(str(self))
        sys.stdout.flush()

    def __str__(self):
        out = [
            tabulate(sorted(self.config.items()), headers=['name', 'value']),
            '({})'.format(self.path)
        ]
        return '\n'.join(out)
