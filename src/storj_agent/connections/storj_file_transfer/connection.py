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
"""Scaffold connection and channel."""
from typing import Any, Optional

import boto3
from aea.configurations.base import PublicId
from aea.connections.base import BaseSyncConnection
from aea.mail.base import Envelope

"""
Choose one of the possible implementations:

Sync (inherited from BaseSyncConnection) or Async (inherited from Connection) connection and remove unused one.
"""

CONNECTION_ID = PublicId.from_str("eightballer/storj_file_transfer:0.1.0")

from packages.eightballer.protocols.file_storage.message import \
    FileStorageMessage


class StorjSyncConnection(BaseSyncConnection):
    """Proxy to the functionality of the SDK or API."""

    MAX_WORKER_THREADS = 5

    connection_id = CONNECTION_ID

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pragma: no cover
        """
        Initialize the connection.

        The configuration must be specified if and only if the following
        parameters are None: connection_id, excluded_protocols or restricted_to_protocols.

        Possible arguments:
        - configuration: the connection configuration.
        - data_dir: directory where to put local files.
        - identity: the identity object held by the agent.
        - crypto_store: the crypto store for encrypted communication.
        - restricted_to_protocols: the set of protocols ids of the only supported protocols for this connection.
        - excluded_protocols: the set of protocols ids that we want to exclude for this connection.

        :param args: arguments passed to component base
        :param kwargs: keyword arguments passed to component base
        """

        self.storj_creds = kwargs.get("configuration").config["storj_creds"]
        self.target_skill = kwargs.get("configuration").config["target_skill_id"]
        super().__init__(*args, **kwargs)

    def main(self) -> None:
        """
        Run synchronous code in background.

        SyncConnection `main()` usage:
        The idea of the `main` method in the sync connection
        is to provide for a way to actively generate messages by the connection via the `put_envelope` method.

        A simple example is the generation of a message every second:
        ```
        while self.is_connected:
            envelope = make_envelope_for_current_time()
            self.put_enevelope(envelope)
            time.sleep(1)
        ```
        In this case, the connection will generate a message every second
        regardless of envelopes sent to the connection by the agent.
        For instance, this way one can implement periodically polling some internet resources
        and generate envelopes for the agent if some updates are available.
        Another example is the case where there is some framework that runs blocking
        code and provides a callback on some internal event.
        This blocking code can be executed in the main function and new envelops
        can be created in the event callback.
        """
        pass

    def on_send(self, envelope: Envelope) -> None:
        """
        Send an envelope.

        :param envelope: the envelope to send.
        """
        if envelope.message.performative == FileStorageMessage.Performative.FILE_UPLOAD:
            self.logger.info(f"Envelope got! {envelope}")
            self._upload(envelope)
        else:
            self.logger.error(
                f"Unsupported performative! {envelope.message.performative}"
            )
            raise NotImplementedError

    def _upload(self, envelope: Envelope) -> None:
        self.logger.info(f"Message got! {envelope.message.content[:100]}")
        extension = envelope.message.filename.rsplit(".", 1)[1]

        self.s3.put_object(
            Body=envelope.message.content.decode("utf-8"),
            Bucket=self.bucket_name,
            Key=envelope.message.key + "." + extension,
        )
        url = self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": envelope.message.key + "." + extension,
            },
            ExpiresIn=604800,
        )
        msg = FileStorageMessage(
            performative=FileStorageMessage.Performative.FILE_DOWNLOAD,
            content=envelope.message.content,
            access_url=url,
        )
        msg.sender = envelope.to
        msg.to = envelope.sender
        file_download_envolope = Envelope(to=msg.to, sender=msg.sender, message=msg)
        self.put_envelope(file_download_envolope)

    def on_connect(self) -> None:
        """
        Tear down the connection.

        Connection status set automatically.
        """
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=self.storj_creds["aws_access_key_id"],
            aws_secret_access_key=self.storj_creds["aws_secret_access_key"],
            endpoint_url=self.storj_creds["endpoint_url"],
        )

        self.bucket_name = "bucketto"
        try:
            self.logger.info(f"creating bucket {self.bucket_name}...")
            self.s3.create_bucket(Bucket="bucketto")
        except self.s3.exceptions.BucketAlreadyExists:
            self.logger.info("bucket already exists")

    def on_disconnect(self) -> None:
        """
        Tear down the connection.

        Connection status set automatically.
        """
        pass
