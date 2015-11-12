FROM vie_apache_proxy

RUN apt-get install -y supervisor python-pip

RUN pip install supervisor-stdout

COPY ./supervisord.conf /etc/supervisor/

CMD ["/usr/bin/supervisord"]
