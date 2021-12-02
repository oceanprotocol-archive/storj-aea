## Install and run

```
git clone git@gitlab.com:datarella/MOBIX-GROUP/storj-aea.git
make new_env
make install_env
```

to run the project you will need a ``.env`` file with the following contents:
```
STORJ_ENDPOINT=""
STORJ_ACCESS_KEY=""
STORJ_ACCESS_KEY_ID=""
TARGET_SKILL="eightballer/storg_file_transfer:0.1.0"
```

run the agent:

```
make run_app
```