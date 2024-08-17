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

## 5 - Accounts

1. `python manage.py startapp accounts`
2. settings.py
   ```python
   # settings.py
   
   INSTALLED_APPS += [
       'accounts.apps.AccountsConfig',
   ]
   
   AUTH_USER_MODEL = 'accounts.User'
   ```
2. class User(AbstractBaseUser)
3. class MyUserManager(BaseUserManager)
4. class UserCreationForm(forms.ModelForm)
5. class CustomUserAdmin(UserAdmin)
7. `python manage.py createsuperuser`
8. Добавил в модель User уникальную комбинация `first_name` и `last_name`

## 6 - REST API и Django REST Framework (DRF) + Системы аутентификации в DRF на JWT

1. `pip install djangorestframework`
2. `pip install djangorestframework-simplejwt`
3. settings.py
   ```python
   # settings.py
   
   INSTALLED_APPS += [
      'accounts.apps.AccountsConfig',
      'rest_framework',
      'rest_framework_simplejwt',
   ]

   # JWT-аутентификация
   REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
         'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
   }
   ```
4. API. Регистрация пользователя
   + class RegisterSerializer(serializers.ModelSerializer)
   + class RegisterView(generics.CreateAPIView)
   ```python
   urlpatterns = [
       path('register/', RegisterView.as_view(), name='register'),
   ]
   ```
   + API http://127.0.0.1:8000/api/register/
   + Content:
   ```python
   {
    "email": "",
    "password": "",
    "first_name": "",
    "last_name": ""
   }
   ```

## 6 - To-Do List

1. `python manage.py startapp todolist`
   ```python
   # settings.py
   
   INSTALLED_APPS += [
      'todolist',
   ]

   ```
2. Модели: Task, Comment, Tag, Category
