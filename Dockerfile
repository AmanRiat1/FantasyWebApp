FROM python:3
RUN mkdir /app
COPY . /app
WORKDIR /app/FantasyWebApp/FantasyApp
COPY requirements.txt /app/
RUN pip install -r requirements.txt

