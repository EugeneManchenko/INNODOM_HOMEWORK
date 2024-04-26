from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'