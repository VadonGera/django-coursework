from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Необходимо указать адрес электронной почты')

        # email = self.normalize_email(email)
        # user = self.model(email=email)
        # user.password = make_password(password)

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='e-mail', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator(
        regex=r'^((\+7)|8)\d{10}$',
        message="Номер телефона должен быть введен в формате: '+79999999999' or '89999999999'.",
    )
    phone_number = models.CharField(
        verbose_name='телефон',
        validators=[phone_regex],
        max_length=12,
        null=True,
        blank=True,
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Есть ли у пользователей конкретное разрешение?"""
        return True

    def has_module_perms(self, app_label):
        """Есть ли у пользователя разрешения на просмотр приложения `app_label`?"""
        return True

    @property
    def is_staff(self):
        """Является ли пользователь сотрудником?"""
        # Допускаем: все администраторы - это сотрудники
        return self.is_admin
