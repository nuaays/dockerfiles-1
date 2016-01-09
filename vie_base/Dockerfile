FROM ubuntu

RUN apt-get update
RUN apt-get install -y supervisor python-pip git-all

RUN pip install supervisor-stdout
RUN mkdir -p /etc/supervisor/conf-available

COPY ./supervisord.conf /etc/supervisor/
COPY ./supervisor_enable_conf.py /usr/sbin/
COPY ./cron.conf /etc/supervisor/conf-available
RUN chmod u+x /usr/sbin/supervisor_enable_conf.py
RUN supervisor_enable_conf.py cron

ENTRYPOINT ["/usr/bin/supervisord"]
