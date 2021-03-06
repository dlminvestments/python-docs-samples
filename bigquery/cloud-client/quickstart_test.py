# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import pytest

import quickstart


# Must match the dataset listed in quickstart.py (there's no easy way to
# extract this).
DATASET_ID = 'my_new_dataset'


@pytest.fixture
def temporary_dataset():
    """Fixture that ensures the test dataset does not exist before or
    after a test."""
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(DATASET_ID)

    if dataset_exists(dataset_ref, bigquery_client):
        bigquery_client.delete_dataset(dataset_ref)

    yield

    if dataset_exists(dataset_ref, bigquery_client):
        bigquery_client.delete_dataset(dataset_ref)


def dataset_exists(dataset, client):
    try:
        client.get_dataset(dataset)
        return True
    except NotFound:
        return False


def test_quickstart(capsys, temporary_dataset):
    quickstart.run_quickstart()
    out, _ = capsys.readouterr()
    if DATASET_ID not in out:
        raise AssertionError
