FROM python:3.12 as base

WORKDIR /app
COPY . /app

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000", "--reload"]