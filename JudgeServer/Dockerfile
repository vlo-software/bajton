FROM judger-docker-base

RUN cp -rf /usr/toolchains/stable-x86_64-unknown-linux-gnu/lib/* /usr/lib
RUN npm -g install typescript && npm -g install @types/node && npm -g install ts-node
HEALTHCHECK --interval=5s --retries=3 CMD python3 /code/service.py
ADD server /code
WORKDIR /code
RUN gcc -shared -fPIC -o unbuffer.so unbuffer.c
EXPOSE 8080
ENTRYPOINT /code/entrypoint.sh
