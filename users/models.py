from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import NULLABLE


class User(AbstractUser):
    verify_token = models.CharField(max_length=35, verbose_name='Токен верификации',
                                    **NULLABLE)
    verify_token_expired = models.DateTimeField(**NULLABLE,
                                                verbose_name='Дата истечения токена')

    username = None
    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
