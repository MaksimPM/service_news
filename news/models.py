from django.db import models


class NewsCategories(models.Model):
    title = models.CharField(max_length=100, verbose_name='категория')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.CharField(max_length=1000, verbose_name='содержание')
    categories = models.ManyToManyField(NewsCategories)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
