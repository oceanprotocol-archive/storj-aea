## Demo 

You are probably already running the agent in one of your terminals. To further test out and demo the agent, you can just add a file to the `upload_dir` directory and watch for the agent's output in the terminal and the StorJ gateway URL for your publicly available file.


```bash
make run_app
```
This will give the following expected output

```
pipenv run app
Loading .env environment variables...
    _     _____     _    
   / \   | ____|   / \   
  / _ \  |  _|    / _ \  
 / ___ \ | |___  / ___ \ 
/_/   \_\|_____|/_/   \_\
                         
v1.1.0

Starting AEA 'storj_agent' in 'async' mode...
info: [storj_agent] creating bucket bucketto...
info: [storj_agent] bucket already exists
info: [storj_agent] setting up down storj handler 
info: [storj_agent] setting up storj behaviour
info: [storj_agent] Start processing messages...

```

In another terminal you can create a file to be used to be uploaded to Storj.

```

echo "Hello World." > src/storj_agent/upload_dir/new_file.txt

```
The file will be uploaded as an asset to Storj and the expected output from the running agent is shown below;

```
info: [storj_agent] Not already uploaded file.. Uploading.
info: [storj_agent] Sender ID eightballer/storj_file_uploader:0.1.0
info: [storj_agent] Envelope got! Envelope(to=eightballer/storj_file_transfer:0.1.0, sender=eightballer/storj_file_uploader:0.1.0, protocol_specification_id=mobix/file_storage:0.1.0, message=Message(sender=eightballer/storj_file_uploader:0.1.0,to=eightballer/storj_file_transfer:0.1.0,content=b'Hello World.\n',dialogue_reference=('', ''),filename=./upload_dir/new_file.txt,key=770b95bb61d5b0406c135b6e42260580,message_id=1,performative=file_upload,target=0))
info: [storj_agent] Message got! b'Hello World.\n'
info: [storj_agent] receieved new url and saved in strategy https://gateway.eu1.storjshare.io/bucketto/770b95bb61d5b0406c135b6e42260580.txt?AWSAccessKeyId=jx7bgg74ceog3eznrovaiqcy23sa&Signature=33sPJd5bLz4tjC9bsJLuMz1py%2Fg%3D&Expires=1639058879
```

The url can then be used to access the file as so;

```bash
tom@gefion~/D/c/d/m/m/p/O/storj_agent> curl "https://gateway.eu1.storjshare.io/bucketto/770b95bb61d5b0406c135b6e42260580.txt?AWSAccessKeyId=jx7bgg74ceog3eznrovaiqcy23sa&Signature=33sPJd5bLz4tjC9bsJLuMz1py%2Fg%3D&Expires=1639058879"
Hello World.
```

![type:video](./content/videos/demo_video.mp4)
