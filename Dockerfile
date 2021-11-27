FROM python:3.6

#RUN mkdir -p /usr/src/app/

ENV PYTHONUNBUFFERED 1
WORKDIR /glider
ADD ./glider

RUN pip install -r requirements.txt

COPY . /manage.py
#
#
#CMD ["python", "manage.py"]