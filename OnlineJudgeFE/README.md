# Bajton Frontend

## Development

### Prerequisite

- Node (14 or 16)

- Yarn (you can use npm instead)

### Linux

```bash
yarn
# we use webpack DllReference to decrease the build time,
# this command only needs to execute once unless you upgrade the package in build/webpack.dll.conf.js
export NODE_ENV=development 
yarn build:dll

# the dev-server will set proxy table to your backend
export TARGET=http://Your-backend

# serve with hot reload at localhost:8080
yarn dev
```
### Windows

```ps
yarn
# we use webpack DllReference to decrease the build time,
# this command only needs to execute once unless you upgrade the package in build/webpack.dll.conf.js
$env:NODE_ENV='development' 
yarn build:dll

# the dev-server will set proxy table to your backend
$env:TARGET='http://Your-backend'

# serve with hot reload at localhost:8080
yarn dev
```

## LICENSE

[MIT](http://opensource.org/licenses/MIT)
