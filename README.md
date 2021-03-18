Для того, чтобы это сработало нужно сначала поднять docker-compose
```bash
docker-compose up
```

Сделать миграцию в бд
```bash
docker-compose exec backend python manage.py makemigrations
```

Накатить на бд миграцию
```bash
docker-compose exec backend python manage.py migrate
```

Создать суперпользователя
```bash
docker-compose exec backend python manage.py createsuperuser
```

Суперпользователя для тестовой бд `admin: admin`
