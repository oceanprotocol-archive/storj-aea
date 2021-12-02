# STORJ AEA For Uploading FIles Through the S3 Compatible Gateway

This agent is responsible for doing an automatic upload of files to the decentralized storage grid StorJ using their S3 compatible gateway.

The following list briefly explains the steps which the agent takes:

- Once this agent is started, it tries to create a new bucket on StorJ if it isn't created already. 
- After the bucket is ready (it already exists or it is created) the agent sets up the storj handler and behaviour
- Starts listening to the upload directory (`src/storj_agent/upload_dir`)
- Once a file is ready in the directory the storj_file_transfer protocol fires a message to the StorJ connection
- The message is proccessed and the file is uploaded to StorJ
- The agent generates a publicly available URL for the file uploaded

This flow is visualized in *Strategy Flow*.

For this demo we use the S3 Compatible Gateway for StorJ. *Note that there are connection variables that you need to provide in the .env file to run this agent successfully with StorJ. Check the Readme for more*.
This agent is available under `src/storj_agent`.

### `eightballer/storj_file_transfer:0.1.0` Connection

This connection acts as a translation layer between the agent and the StorJ storage grid. 
The main task of this connection is to connect and mediate the file transfers to Storj.

### `eightballer/storj_file_uploader:0.1.0` Skill

Very simple behaviour where the agent reads and searializes the file that needs to be uploaded into an Envelope with bytes content.

### `eightballer/file_storage:0.1.0` Protocol

This protocol is in place to allow for communication between the different components of the agent, in this case between the above mentioned connection and skill.