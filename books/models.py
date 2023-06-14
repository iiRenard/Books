from django.db import models


class Articles(models.Model):
    name = models.CharField('Название книги', max_length=50)
    author = models.CharField('Автор книги', max_length=150)
    translator = models.CharField('Переводчик', max_length=250)
    publishing = models.CharField('Издательство', max_length=250)
    series = models.CharField('Серия', max_length=250)
    genre = models.CharField('Жанр книги', max_length=150)
    years = models.CharField('Возрастное ограничение', max_length=150)
    rating = models.CharField('Популярность книги', max_length=50)
    comment = models.TextField('Описание книги')
    price = models.CharField('Стоимость', max_length=50)
    pages = models.CharField('Страницы', max_length=250)
    weight = models.CharField('Масса', max_length=250)
    dimensions = models.CharField('Размеры', max_length=250)
    pub_date = models.DateField('Дата публикации книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
