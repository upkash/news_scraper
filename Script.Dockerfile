FROM python:3
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y cron
RUN touch /var/log/cron.log
WORKDIR /
COPY ./app/usnews.py /usnews.py
COPY script_requirements.txt /tmp/requirements.txt
COPY cronjob /etc/cron.d/cjob
RUN chmod 0644 /etc/cron.d/cjob
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt
ENV PYTHONUNBUFFERED 1
CMD cron -f