FROM python:3.8
# FROM gcr.io/google-appengine/python:latest

# RUN mkdir /app

# COPY . /app

WORKDIR /app

ADD . /app/

# RUN pip install --no-cache-dir --upgrade pip
RUN pip install protobuf grpcio-tools

# CMD ["python" , "./app/main.py"]
ENTRYPOINT ["python" ,"-u", "./main.py"]
