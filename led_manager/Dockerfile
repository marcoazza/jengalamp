FROM alexellis2/python-gpio-arm:armv6
COPY ./requirements.txt /requirements.txt
RUN apt-get -q update && \
    apt-get -qy install python3-dev python3-pip gcc make && \
    apt-get -o Dpkg::Options::="--force-confmiss" install --reinstall netbase && \
    pip3 install -r /requirements.txt && \
    apt-get -qy remove python3-dev gcc make && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qy clean all && \
    apt-get -qy autoremove && \
    mkdir /app

COPY . /app
CMD ["python3", "/app/main.py"]