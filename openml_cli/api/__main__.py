# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os
from dotenv import load_dotenv

from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file


def main():

    # Load config:
    SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    load_dotenv(dotenv_path=os.path.join(SRC_DIR, '..', '.env'), override=True)

    OPENML_API_KEY = os.getenv('OPENML_API_KEY')

    http_client = RequestsClient()
    http_client.set_api_key(
        'www.openml.org', OPENML_API_KEY,
        param_name='api_key', param_in='header'
    )

    swagger_defs = os.path.join(SRC_DIR, 'swagger.yml')
    client = SwaggerClient.from_spec(load_file(swagger_defs),
                                     http_client=http_client)

    # Dataset:
    result = client.dataset.getDataSetById(id=10).response().result
    print(result.data_set_description.name)

    # Dataset features:
    result = client.dataset.getDataFeaturesById(id=10).response().result
    print(result.data_features.feature[0].name)


if __name__ == "__main__":
    # load_dotenv(find_dotenv(), override=True)
    main()
