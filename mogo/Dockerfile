FROM mongodb:latest

RUN mkdir -p /data/db2 \
    && echo "dbpath = /data/db2" > /etc/mongodb.conf \
    && chown -R mongodb:mongodb /data/db2

COPY . /data/db2

RUN mongod --replSet=bigchain-rs --fork --logpath /var/log/mongodb.log --dbpath /data/db2 --smallfiles\
    && CREATE_FILES=/data/db2/scripts \