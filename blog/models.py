from django.db import models

from base.models import NULLABLE


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE)
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
