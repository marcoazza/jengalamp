FROM alexellis2/python-gpio-arm:armv6
RUN apt-get -q update && \
    apt-get -qy install python3-dev python3-pip gcc make && \
    mkdir /app

COPY . /app

RUN pip3 install -r /app/requirements.txt && \
    apt-get -qy remove python3-dev gcc make && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qy clean all && \
    apt-get -qy autoremove
CMD ["python3", "main.py"]