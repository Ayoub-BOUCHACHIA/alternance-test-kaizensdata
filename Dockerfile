# syntax=docker/dockerfile:1
FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip 
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python","manage.py","runserver"]

