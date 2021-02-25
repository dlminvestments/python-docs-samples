# Copyright 2015 Google Inc. All Rights Reserved.
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

import os

import pytest

import main


@pytest.mark.skipif(
    not os.path.exists('/usr/games/fortune'),
    reason='Fortune executable is not installed.')
def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    if r.status_code != 200:
        raise AssertionError
    if not len(r.data):
        raise AssertionError
