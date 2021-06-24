FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD manage.py /code/
RUN pip3 install -r requirements.txt
COPY /scripts/scripts.sh /
ADD . /code/