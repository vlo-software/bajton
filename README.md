# Bajton

### An online education system based on the [OnlineJudge 2.0](https://github.com/QingdaoU/OnlineJudge) by Qingdao University.

[See the website](https://bajton.vlo.gda.pl)

## Added features

- Added support for `C#`, `Perl` and `BrainF**k`.

- Updated `Java` and `Python3` to the newest version.

- The UI was redesigned.

- Most of the `iView` components have been rewritten in our own `BajtonUI` library.

- The users can now see the output of the first two tests when viewing their submission.

- And many others.

## Installation

### Prerequisite

- Git

- Docker

- Docker-Compose

- NodeJS (NVM is recommended)

- Yarn (you can use npm instead)

### Linux

First, you need to clone this repository:

```sh
git clone https://github.com/vlo-software/bajton.git
```

Then, you have to enter the newly created `bajton` directory:

```sh
cd ./bajton
```

The next step is to build the OnlineJudge frontend:

> The frontend is built using NodeJS 14, so you have to use NVM to install it.

```sh
nvm install 14 && nvm use 14
```

```sh
cd ./OnlineJudgeFE && yarn && yarn build:dll && yarn build
```

After that, you need to copy the `dist` directory to the `OnlineJudge` folder:

```sh
cp -rf ./dist ../OnlineJudge/dist
```

And replace the CDN related lines

```sh
cd ../OnlineJudge/dist && find . -name "*.*" -type f -exec sed -i "s/__STATIC_CDN_HOST__\///g" {} \; && cd ../../
```

Next, you have to build the Baza Wiedzy frontend:

> The Baza Wiedzy is built using NodeJS 18, so you have to use NVM to install it.

```sh
nvm install 18 && nvm use 18
```

```sh
cd ./BazaWiedzy && yarn && yarn build && cd ../
```

Now, you have to build the docker image used by the `JudgeServer` service:

```sh
cd ./JudgeServer/docker-base && sudo docker build -t judger-docker-base . && cd ../../
```

> Before the final step, you should edit the token that you will find in the `OnlineJudgeDeploy/docker-compose.yml`.

With all the preparation completed, you can finally deploy the project:

```sh
cd OnlineJudgeDeploy && sudo docker-compose up -d
```

### Windows

First, you need to enable the WSL2 integration in Docker.

Then you have to use the WSL2 (Ubuntu) and follow the instructions for Linux.

> Windows by default will try to convert the line endings to CRLF, which will break the build process. You have to disable that in your git config and reset the repository:

```sh
git config core.autocrlf false
git rm --cached -r .
git reset --hard
```

The only difference is that you have to use a different command to run the docker-compose:

```sh
sudo docker-compose -f docker-compose.yml -f docker-compose_win.yml up -d
```

> Because of the limitations of docker on Windows, Postgres has to be mounted in a virtual volume, the `docker-compose_win.yml` file takes care of that.

## Development

The steps for running in development are the same as for installation, except that you have to use a different docker-compose file:

#### Linux

```sh
sudo docker-compose -f docker-compose.yml -f docker-compose_dev.yml up
```

#### Windows

```sh
sudo docker-compose -f docker-compose.yml -f docker-compose_dev.yml -f docker-compose_win.yml up
```

#

### Running tests

In order to test the Baza Wiedzy you need to run the production build, and then run the tests:

```sh
sudo ./BazaWiedzy/run_tests.sh
```

## Contribution

### Branch naming convention

The branch name should start with the issue type, followed by the issue number and a short description of the task divided by dashes.

For example, if you are working on issue number 42, which is a bug, and you are fixing the login form, the branch name should be `bug-42-fix-login-form`.

The issue type can be one of the following:

- `bug` - a bug that needs to be fixed

- `feature` - a new feature that needs to be implemented

- `refactor` - a part of the code that needs to be refactored

- `docs` - a part of the documentation that needs to be updated

### Team members

Most of the work is done through the GitHub project board, so if you are a part of our team, you can find the tasks there.

Choose one of the tasks from the `Ready` column that you want to work on, make sure you are one of the assigned people, and create a new branch following our naming convention.

When you are done, create a pull request to the `dev` branch, make sure you link it with the issue, move the task to the `In review` column in the project, and request a review from [Capure](https://github.com/orgs/vlo-software/people/Capure) or [0ZeroFive5](https://github.com/0ZeroFive5).

### Others

If you are not a part of our team, you can contribute to this project by opening an issue or creating a pull request for an existing one.

Make sure to follow the branch naming convention.

## License

[MIT](https://opensource.org/licenses/MIT)
