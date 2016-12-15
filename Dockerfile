FROM ubuntu:16.04


COPY debian/deps.txt /
RUN apt-get update \
    && cat deps.txt | xargs apt-get install -y  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY debian/requirements.txt /
RUN pip3 install -r requirements.txt

RUN service postgresql restart

COPY sql/init.sh /
RUN ./init.sh
