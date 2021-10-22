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

"""This package contains a scaffold of a behaviour."""
import glob
import os
from typing import cast

from aea.mail.base import Envelope
from aea.skills.behaviours import TickerBehaviour
from packages.eightballer.skills.storj_file_uploader import \
    PUBLIC_ID as SENDER_ID
from packages.eightballer.skills.storj_file_uploader.dialogues import \
    DefaultDialogues
from packages.fetchai.protocols.default.message import DefaultMessage


class StorjFileUploadBehaviour(TickerBehaviour):
    """This class scaffolds a behaviour."""

    def __init__(self, *args, **kwargs):
        self._upload_dir = kwargs.pop("upload_dir")
        super().__init__(*args, **kwargs)

    def setup(self) -> None:
        """Implement the setup."""
        self.log = self.context.logger.info
        self.log(f"setting up storj behaviour")

    def act(self) -> None:
        """Implement the act."""
        self.log(f"acting in storj behaviour")

        available_files = glob.glob("./upload_dir/*")
        for file in available_files:
            file_bytes = open(file, "rb").read()
            self.log(f"File found in directory. {file_bytes}")
            self.__create_envelope(file_bytes, file)

    def __create_envelope(self, bytes, filename) -> None:
        receiver_id = "eightballer/storj_file_transfer:0.1.0"
        self.log(f"Sender ID {SENDER_ID}")
        msg = DefaultMessage(
            performative=DefaultMessage.Performative.BYTES, content=bytes
        )
        msg.sender = str(SENDER_ID)
        msg.to = receiver_id
        file_upload_envolope = Envelope(
            to=receiver_id, sender=str(SENDER_ID), message=msg
        )
        self.context.outbox.put(file_upload_envolope)

    def teardown(self) -> None:
        """Implement the task teardown."""
        self.log(f"Tearing down storj behaviour")
