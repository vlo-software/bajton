#!/bin/bash

npx prisma generate

if [ "$BAJTON_ENV" == "dev" ]; then
		echo "Running in dev mode";
		yarn dev;
else
		echo "Running in prod mode";
		yarn start;
fi