FROM php:7.4-apache

WORKDIR /var/www/html

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN  echo "SparkCTF{648098eb7a379e92ae6b0e709408d37bf8cda0e49c99794004f0ce30e4874d03}" > "/tmp/flag" && chown www-data:www-data "/tmp/flag"

COPY index.php /var/www/html

EXPOSE 1587
