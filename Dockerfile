FROM postgres:14

ADD ./scripts/create-db.sql /docker-entrypoint-initdb.d/
ADD ./scripts/data.csv /data.csv