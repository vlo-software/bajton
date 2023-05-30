FROM python:3.7-alpine3.9

ENV OJ_ENV dev 

HEALTHCHECK --interval=5s --retries=3 CMD python2 /app/deploy/health_check.py

ADD ./deploy/requirements.txt /app/deploy/requirements.txt

RUN apk add --update --no-cache build-base nginx openssl curl unzip supervisor jpeg-dev zlib-dev postgresql-dev freetype-dev && \
    pip install --no-cache-dir -r /app/deploy/requirements.txt && \
    apk del build-base --purge

WORKDIR /app

ENTRYPOINT /app/deploy/entrypoint.sh

