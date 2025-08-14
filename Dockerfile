FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=0 \
    DJANGO_SETTINGS_MODULE=UpTraderTZ.settings

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

# Создаем директорию для статических файлов
RUN mkdir -p staticfiles

# Собираем статические файлы
RUN python manage.py collectstatic --noinput --verbosity=0

# Проверяем, что файлы собраны
RUN ls -la staticfiles/
RUN ls -la staticfiles/menu/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "UpTraderTZ.wsgi:application"]