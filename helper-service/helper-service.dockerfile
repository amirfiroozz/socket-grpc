FROM python:3.8

WORKDIR /app

ADD . /app/

RUN pip install protobuf grpcio-tools

ENTRYPOINT ["python" ,"-u", "./main.py"]
