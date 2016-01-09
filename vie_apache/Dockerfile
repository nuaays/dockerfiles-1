FROM vie_base

RUN apt-get install -y apache2

# Apache config
RUN a2dissite 000-default
RUN a2enmod file_cache cache cache_disk dump_io reqtimeout include mime_magic \
    expires headers usertrack unique_id asis info cgi actions rewrite

RUN echo 'export HOSTNAME=$(hostname)' >> /etc/apache2/envvars

COPY ./apache.conf /etc/supervisor/conf-available/
RUN supervisor_enable_conf.py apache

EXPOSE 80 443
