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
sudo docker-compose -f docker-compose_dev.yml up
```

#### Windows

```sh
sudo docker-compose -f docker-compose_dev.yml -f docker-compose_win.yml up
```

#

### Running tests

In order to test the Baza Wiedzy you need to run the production build, and then run the tests:

```sh
cd ./BazaWiedzy && sudo ./run_tests.sh && cd ../
```

## Contribution

If you want to contribute to this project, open an issue or create a pull request for an existing one.

There are no official guidelines as far as coding conventions are concerned.

Just follow your common sense :wink: .

## License

[MIT](https://opensource.org/licenses/MIT)
