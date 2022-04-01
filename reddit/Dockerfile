FROM ubuntu:20.04

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt

CMD ["python3", "reddit/main.py"]