FROM vie_apache_proxy

RUN apt-get install -y supervisor

COPY ./supervisord.conf /etc/supervisor/

CMD ["/usr/bin/supervisord"]
