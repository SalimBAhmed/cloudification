FROM python:3.7
COPY ./app /app
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]