# Copyright 2016 Google Inc. All rights reserved.
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

import mock
import pytest


@pytest.fixture
def app(monkeypatch):
    monkeypatch.setenv('SENDGRID_API_KEY', 'apikey')
    monkeypatch.setenv('SENDGRID_SENDER', 'sender@example.com')

    import main

    main.app.testing = True
    return main.app.test_client()


def test_get(app):
    r = app.get('/')
    if r.status_code != 200:
        raise AssertionError


@mock.patch('python_http_client.client.Client._make_request')
def test_post(make_request_mock, app):
    response = mock.Mock()
    response.getcode.return_value = 200
    response.read.return_value = 'OK'
    response.info.return_value = {}
    make_request_mock.return_value = response

    app.post('/send/email', data={
        'to': 'user@example.com'
    })

    if not make_request_mock.called:
        raise AssertionError
    request = make_request_mock.call_args[0][1]
    if 'user@example.com' not in request.data.decode('utf-8'):
        raise AssertionError
