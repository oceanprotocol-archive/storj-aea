# Protocols

### `eightballer/storj_file_transfer:0.1.0` Connection

This connection acts as a translation layer between the agent and the StorJ storage grid. 
The main task of this connection is to connect and mediate the file transfers to Storj.

### `eightballer/storj_file_uploader:0.1.0` Skill

Very simple behaviour where the agent reads and serializes the file that needs to be uploaded into an Envelope with bytes content.

### `eightballer/file_storage:0.1.0` Protocol

This protocol is in place to allow for communication between the different components of the agent, in this case between the above-mentioned connection and skill.