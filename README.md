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

- NodeJS (14 or 16)

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

The next step is to build the frontend:

```sh
cd ./OnlineJudgeFE && yarn && yarn build:dll && yarn build
```

After that, you need to copy the `dist` directory to the `OnlineJudge` folder:

```sh
cp -rf ./dist ../OnlineJudge/dist
```

When that's done, you can go back to the root directory of the project:

```sh
cd ..
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

You have to follow the instructions for Linux, with one caveat, the way docker works on windows prevents the Postgres database from functioning properly when configured the way it's configured in our project.

The solution is to mount a physical drive formatted as ext4 and keep the project on that drive.

> Note this is only possible on windows 11

## Contribution

If you want to contribute to this project, open an issue or create a pull request for an existing one.

There are no official guidelines as far as coding conventions are concerned.

Just follow your common sense :wink: .

## License

[MIT](https://opensource.org/licenses/MIT)