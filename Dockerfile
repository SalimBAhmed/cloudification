FROM python:3.7
COPY ./app /app
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "app/main.py"]