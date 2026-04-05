FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 8050
EXPOSE 8051

CMD ["uvicorn", "app.main:app", "--host","0.0.0.0", "--port", "8000"]
