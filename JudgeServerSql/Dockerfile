FROM node:16-alpine3.14

WORKDIR /app

COPY . /app

RUN yarn

RUN yarn build

ENV NODE_ENV production

CMD yarn start