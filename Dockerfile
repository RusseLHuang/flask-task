FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.7 libpython3.7-dev

WORKDIR /app

COPY requirements.txt /app

RUN python3.7 -m pip install --no-cache-dir -r requirements.txt

COPY config.py /app

COPY wsgi.py /app

COPY wsgi.ini /app

COPY app.py /app

COPY src /app/src

EXPOSE 5000

CMD ["uwsgi", "wsgi.ini"]