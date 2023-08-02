
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . /app/

RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir pre-commit
RUN pre-commit install


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
