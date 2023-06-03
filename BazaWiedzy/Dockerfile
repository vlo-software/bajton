FROM ubuntu:22.04

RUN apt-get update
RUN echo "y" | apt-get install curl
RUN mkdir -p /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v18.16.0
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/bin
ENV PATH $NODE_PATH:$PATH

RUN npm install -g yarn

COPY ./package.json /app/
COPY ./playwright.config.ts /app/

WORKDIR /app
RUN yarn


RUN npx playwright install-deps && npx playwright install

EXPOSE 3000

CMD ./run.sh