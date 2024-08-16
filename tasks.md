## 1 - Init
1. `git init`
2. `requirements.txt`
   + `pip install -r requirements.txt`
3. `.gitignore`
4. `README.md`
5. GitHub
   + git branch -M main
   + git remote add origin https://github.com/VadonGera/django-coursework
   + git push -u origin main

## 2 - Django

1. `django-admin startproject myproject .`
2. `python manage.py runserver`

## 3 - .env

1. `pip install python-decouple`

## 4 - Postgres

1. Запускаем контейнер с PostgreSQL
   + docker run --name db_postgres -e POSTGRES_USER=myadmin -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mypostgres -p 5432:5432 -d postgres
   + Для работы с PostgreSQL через Docker надо остановить службу PostgreSQL в Windows, если она запущена.
2. `pip install "psycopg[binary]"`
3. settings.py
   ```python
   # settings.py
   
   from decouple import config
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': config('DATABASE_NAME'),
           'USER': config('DATABASE_USER'),
           'PASSWORD': config('DATABASE_PASSWORD'),
           'HOST': config('DATABASE_HOST'),
           'PORT': config('DATABASE_PORT', default='5432'),
       }
   }
   ```


## 3 - To-Do List

1. `python manage.py startapp todolist`

## 4 - Accounts

1. `python manage.py startapp accounts`
