# Використовуємо операційну систему Python версії 3.9 в якій встановлюємо Python та потрібні залежності.
FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Встановлюємо залежності для PostgreSQL
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Встановлюємо залежності Python, використовуючи файл `requirements.txt`.
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копіюємо наш Django-проект у контейнер.
COPY . /code/