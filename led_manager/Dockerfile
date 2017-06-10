FROM alexellis2/python-gpio-arm:armv6

WORKDIR /root/

RUN apt-get -q update && \
    apt-get -qy install python3-dev python3-pip gcc make && \
    pip3 install rpi-ws281x && \
    pip3 install unicornhat

COPY lights.py .

RUN apt-get -qy remove python3-dev gcc make && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qy clean all && \
    apt-get -qy autoremove
CMD ["python3", "ligths.py"]