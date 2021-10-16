FROM python:3.7
COPY ./app /app
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]