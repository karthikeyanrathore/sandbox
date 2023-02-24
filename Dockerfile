FROM python:3.8-slim-buster

# WORKDIR /test

ADD sandbox.py /
ADD _test_sandbox.py /

RUN [ "python3", "-u", "_test_sandbox.py"]

