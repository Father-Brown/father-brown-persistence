FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENV FLASK_APP Main.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]

