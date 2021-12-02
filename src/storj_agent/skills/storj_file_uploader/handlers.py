# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This package contains a scaffold of a handler."""

from typing import Optional, cast

from aea.configurations.base import PublicId
from aea.protocols.base import Message
from aea.skills.base import Handler
from packages.eightballer.protocols.file_storage.message import \
    FileStorageMessage
from packages.eightballer.skills.storj_file_uploader.strategy import Strategy


class FileStorageHandler(Handler):
    """This class scaffolds a handler."""

    SUPPORTED_PROTOCOL = FileStorageMessage.protocol_id  # type: Optional[PublicId]

    def setup(self) -> None:
        """Implement the setup."""
        self.log = self.context.logger.info
        self.log(f"setting up down storj handler ")

    def handle(self, message: Message) -> None:
        """
        Implement the reaction to an envelope.

        :param message: the message
        """
        strategy = cast(Strategy, self.context.strategy)

        if message.access_url not in strategy.file_urls.keys():
            strategy.file_urls[message.access_url] = message
            self.log(f"receieved new url and saved in strategy {message.access_url}")

    def teardown(self) -> None:
        """Implement the handler teardown."""
        self.log(f"tearing down storj handler ")
