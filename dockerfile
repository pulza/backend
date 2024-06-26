FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
