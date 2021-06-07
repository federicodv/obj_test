FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1


WORKDIR /app
COPY ./docker-entrypoint.sh /app
ADD ./src /app
EXPOSE 5000

RUN apt-get update
RUN apt-get install -y --no-install-recommends figlet

RUN pip install -r "requirements.txt"
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
