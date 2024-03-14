FROM ubuntu:latest

WORKDIR /app

COPY index.js /app

RUN apt-get update && \
    apt-get install npm -y && \
    npm init -y && \
    npm install express

EXPOSE 8080

CMD ["node", "index.js"]
