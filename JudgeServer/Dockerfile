FROM judger-docker-base

HEALTHCHECK --interval=5s --retries=3 CMD python3 /code/service.py
ADD server /code
ADD tools /tools
WORKDIR /code
RUN gcc -shared -fPIC -o unbuffer.so unbuffer.c
EXPOSE 8080
ENTRYPOINT /code/entrypoint.sh
