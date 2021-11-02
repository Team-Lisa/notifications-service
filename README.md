# notifications-service

[![.github/workflows/pipeline.yml](https://github.com/Team-Lisa/notifications-service/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/Team-Lisa/notifications-service/actions/workflows/pipeline.yml)
[![Coverage Status](https://coveralls.io/repos/github/Team-Lisa/notifications-service/badge.svg?branch=main)](https://coveralls.io/github/Team-Lisa/notifications-service?branch=main)

## Local Mode

#### Requirements

- Python 3.9
- [Poetry](https://python-poetry.org/docs/#installation)

#### Setup
1. run ```poetry install``` 
2. run ```poetry shell``` (create a venv)

#### Running locally
- ```uvicorn api.main:app```

## Using Docker

#### Requirements
- Docker

#### Running locally

1. ```make build``` 
2. ```make start```


## Documentation
You can see the automatic interactive API documentation using the endpoint: ```/docs```

## Repository Setup

You need to configure the following secrets

### Heroku

- ```HEROKU_API_KEY```
- ```HEROKU_APP_NAME```
- ```HEROKU_EMAIL```

### Coveralls

- ```COVERALLS_TOKEN```


### MongoDB

- ```DB_PASSWORD```
