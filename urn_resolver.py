###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################

from flask import abort, Flask, redirect
import requests

app = Flask(__name__)

NID = 'wmo'

NSS_MAP = {
    "md": 'https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items'  # noqa
}


@app.route("/<path:path>")
def urn(path):

    if not path.startswith('urn:'):
        abort(400, 'Invalid / undefined URN')

    _, nid, nss, _ = path.split(':', 3)

    if nid != NID:
        abort(400, 'Invalid namespace identifier (NID)')

    if nss not in NSS_MAP:
        abort(400, 'Invalid namespace specific string (NSS)')

    url = f'{NSS_MAP[nss]}/{path}'

    try:
        response = requests.head(url)
        response.raise_for_status()
    except requests.HTTPError:
        abort(404)

    return redirect(url)
