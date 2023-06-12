# Bajton Baza Wiedzy

## Development

### Running tests

Make sure you are running the production build and then run:

```sh
sudo ./run_tests.sh
```

### Updating the migrations

```sh
sudo docker exec -it bajton-baza-wiedzy npx prisma migrate dev
```

### Common issues

- VS Code complains about missing `prisma` client. Run `yarn` and then `npx prisma generate` on your local machine.

- Changes to prisma middleware require a restart of the server. This is because the middleware is loaded on server start. You can restart the server by running `sudo docker-compose restart bajton-baza-wiedzy` in the `OnlineJudgeDeploy` directory.

- The production build is not up to date. Run `sudo docker exec -it bajton-baza-wiedzy yarn build` to rebuild it and restart the `docker` containers.

- The newly added `npm` package is not present in the `docker` container. You need to rebuild the `docker` image by running `sudo docker-compose build --no-cache` in the `OnlineJudgeDeploy` directory.

### Important notes

Rember to ALWAYS import the prisma client from the `utils/db` file and not directly from the `@prisma/client` package. This is because the `utils/db` file contains the middlewares required for the `prisma` client to work in our project.
