FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /proj
WORKDIR /proj
COPY requirements.txt /proj/
RUN pip install -r requirements.txt
COPY . /proj/
RUN ./manage.py migrate
