# Copyright European Organization for Nuclear Research (CERN) since 2012
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING
from uuid import uuid4

from rucio.daemons.c3po.utils.timeseries import RedisTimeSeries

if TYPE_CHECKING:
    from rucio.common.types import InternalScope


class DatasetCache:
    """
    Utility to count the accesses of the datasets during the last day.
    """
    def __init__(
            self,
            redis_host: str,
            redis_port: int,
            timeout: int = 1,
            prefix: str = 'did_cache',
            delete_keys: bool = False
    ):
        self._prefix = prefix + '_' + str(uuid4()).split('-')[0]
        self._tms = RedisTimeSeries(redis_host, redis_port, timeout, self._prefix)

        if delete_keys:
            self._tms.delete_keys()

    def add_did(self, did: tuple['InternalScope', str]) -> None:
        self._tms.add_point('{}_{}'.format(did[0].internal, did[1]), 1)

    def get_did(self, did: tuple['InternalScope', str]) -> int:
        self._tms.trim()

        series = self._tms.get_series('{}_{}'.format(did[0].internal, did[1]))

        return len(series)
