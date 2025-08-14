# Краткое руководство

## 🚀 Как запустить проект

```bash
git clone https://github.com/wasabi52ngg/uptradertz
cd UpTraderTZ

docker-compose up --build

# Приложение доступно по: http://localhost:8000
```

## Что добавлено

- **Docker контейнеризация** 
- **Docker Compose** - оркестрация Django/Gunicorn + Nginx
- **CI Pipeline** - автоматические тесты через GitHub Actions
- **Автоматические тесты** - проверка доступности страниц и работы меню

## Примечание

- В файле БД уже сохранены обьекты разных меню
- В settings.py прописал CSRF_TRUSTED_ORIGINS чтобы можно было в админке вносить изменения