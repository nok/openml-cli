# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os

from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file


OPENML_API_KEY = os.environ.get('OPENML_API_KEY', False)


http_client = RequestsClient()
http_client.set_api_key(
    'www.openml.org', OPENML_API_KEY,
    param_name='api_key', param_in='header'
)

src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
api_swagger_def = src_dir + os.sep + 'swagger.yml'
client = SwaggerClient.from_spec(load_file(api_swagger_def),
                                 http_client=http_client)

# Dataset:
result = client.dataset.getDataSetById(id=10).response().result
print(result.data_set_description.name)

# Dataset features:
result = client.dataset.getDataFeaturesById(id=10).response().result
print(result.data_features.feature[0].name)
