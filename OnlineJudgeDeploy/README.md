# Deployment tools

This repo contains some useful deployment scripts.

## Contents

#### Shell scripts

- `build.sh` - Builds the front end and the docker-compose services.

- `reset_langs.sh` - You need to run this every time you add a new programming language.

- `./backup/db_backup.sh` - Dumps the entire database to a `.sql` file.

> Note that for the backup to be useful, you also need to copy the `./data` directory created by docker.

#### docker-compose.yml

This is where all the services are configured.

- `oj-redis` - An in-memory database used as a queue for the submissions.

- `oj-postgres` - A relational database where all the user data is stored.

- `judge-server` - A service that runs the submitted code and checks the results.

- `oj-backend` - The backend service is where the REST API lives.