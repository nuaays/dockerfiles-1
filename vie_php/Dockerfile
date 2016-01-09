FROM vie_apache_mysqlclient

RUN apt-get install -y php5 libapache2-mod-php5 php5-redis php5-mcrypt \
    php5-mysql php5-cgi php5-cli

COPY ./php.ini /etc/php5/apache2/
COPY ./php.ini /etc/php5/cli/
COPY ./dir.conf /etc/apache2/mods-available/
RUN php5enmod mcrypt
