FROM php:7.0-apache
COPY web/ /var/www/html/

RUN rm -rf /var/www/html/db;mkdir /var/www/html/db;chmod -R 777 /var/www/html/db; touch /var/www/html/db/index.php;
RUN php /var/www/html/index.php
RUN chmod -R 555 /var/www/html/db
