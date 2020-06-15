From python:3
ENV PYTHONBUFFERED 1
EXPOSE 8000
RUN mkdir /server
WORKDIR /server
COPY requirements.txt /server
RUN pip install -r requirements.txt