[![Build Status](https://img.shields.io/docker/cloud/build/alineem/dice-roll)](https://hub.docker.com/repository/docker/alineem/dice-roll/builds) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# English Database 

This is a Python based english database. The user can input the word (in english) they would like to save and the result is stored on a PostgreSQL database along with the translation (in portuguese) to that word.
The results are also displayed on a table to the user. 

## How to run

### Docker Hub
In order to run this container you'll need docker installed.

#### Mandatory environment variables

Run the following command:

>$ docker run -e ENGLISH_DATABASE_DB_USERNAME="username" -e ENGLISH_DATABASE_DB_PASSWORD="password" -e ENGLISH_DATABASE_DB_HOSTNAME="hostname" -e ENGLISH_DATABASE_DB_PORT="port" -e ENGLISH_DATABASE_DB_NAME="database-name" --rm -p 5000:5000 english-database