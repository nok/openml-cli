# -*- coding: utf-8 -*-

import os
from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file


class API:
    def __init__(self, apikey=None):
        http_client = None
        if apikey:
            http_client = RequestsClient()
            http_client.set_api_key('www.openml.org',
                                    apikey,
                                    param_name='api_key',
                                    param_in='header')
        file_path = os.path.abspath(__file__)
        src_path = os.path.join(os.path.dirname(file_path), '..')
        api_defs = os.path.join(src_path, 'swagger.yml')
        self.client = SwaggerClient.from_spec(load_file(api_defs),
                                              http_client=http_client)
