FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./backend_requirements.txt /tmp/requirements.txt

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app