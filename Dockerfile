FROM python:3
ENV PYTHONUNBUFFERED = 1
WORKDIR /usr/src/app
COPY . .
#COPY requirements.txt ./
#RUN pip uninstall django
RUN pip install --upgrade pip
RUN pip install -r req2.txt
#RUN apt-get install libpq-dev