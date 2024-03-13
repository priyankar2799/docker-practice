FROM python:latest
WORKDIR /app
COPY . /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
