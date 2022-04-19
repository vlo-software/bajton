# JudgeServerSql

This service handles the judging for sql problems.

## Usage

In order to check a submission, you must publish a message to the `judge-server-sql-jobs` channel on redis.

The `JudgeServerSql` will compare the test query with the query provided by the user and return a result for each of the test cases.

The result can be either `passed`, `failed` or `error`.

Each test will be preformed on a freshly initialised database (SQL.js).

The results will be pushed to the `judge-server-sql-results` list on redis.

You can track which submission the results are meant for, by looking at the submissionId.

## Development

First you need to install all the dependencies

```sh
yarn
```

Make sure you have an instance of redis running and start the project with

```sh
yarn dev
```

## Building for production

In order to build for production use

```sh
yarn build
```

You can then start the project with

```sh
yarn start
```