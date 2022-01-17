FROM ubuntu:18.04

COPY build/java_policy /etc
ENV DEBIAN_FRONTEND=noninteractive
RUN buildDeps='software-properties-common git libtool cmake python3-dev python3-pip libseccomp-dev curl' && \
    apt-get update && apt-get install -y python3 python3-pkg-resources $buildDeps && \
    add-apt-repository ppa:longsleep/golang-backports && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    add-apt-repository ppa:ondrej/php && \
    add-apt-repository ppa:deadsnakes/ppa && \
    curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get update && apt-get install -y golang-go python3.10 openjdk-17-jre-headless php-cli nodejs gcc-9 g++-9 unzip && \
    update-alternatives --install  /usr/bin/gcc gcc /usr/bin/gcc-9 40 && \
    update-alternatives --install  /usr/bin/g++ g++ /usr/bin/g++-9 40 && \
    apt-get install -y openjdk-17-jre openjdk-17-jdk mono-complete && \
    pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -I --no-cache-dir psutil gunicorn flask requests idna && \
    cd /tmp && git clone -b newnew  --depth 1 https://gitee.com/qduoj/Judger.git && cd Judger && \
    mkdir build && cd build && cmake .. && make && make install && cd ../bindings/Python && python3 setup.py install && \
    apt-get purge -y --auto-remove $buildDeps && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    mkdir -p /code && \
    useradd -u 12001 compiler && useradd -u 12002 code && useradd -u 12003 spj && usermod -a -G code spj