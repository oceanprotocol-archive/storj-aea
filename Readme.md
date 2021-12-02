# AEA Storj File Uploader

## Prerequisites

To setup the project, make sure you have the latest verson of pipenv first:
```
pip install -U pipenv
```

We advise running on Linux based machine or WSL.

Make sure you have ``make`` as well:
```
sudo apt-get install build-essential
```

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


# Components

- gitlab ci
    - The ci contains the basic configuration required to launch a launch a gitlab ci
  
- Dockerfile
  - Basic Dockerfile which installs deps and launchs the app

- makefile
  - lints
      - isort
      - black
      - code clean
- pre-commit hooks for the build process

- scripts
  - app.py launcher for debugging and launching docker process

- Pipfile

- gitignore
- docker ignore
- .env file
- docs


# Example running docs

1. clone repo
2. setup a new environment
   - make new_env
   - make 
3. in project directory:
```bash
 mkdocs serve
```
Visit http://127.0.0.1:8000/  

# Install environment
1. install pip
```
pip install pipenv
```

2. create new environment
```
make new_env
```
3. install new env
```
make install_env
```



# dev tools
setup pre-commit hooks
```
make install_hooks
```

lint, format, and sense check code
```
make lint
```

run tests

```
make tests
```

