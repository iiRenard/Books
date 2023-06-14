from .models import Articles
from django.forms import ModelForm, TextInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'author', 'translator', 'publishing', 'series', 'genre',
                  'years', 'rating', 'comment', 'price', 'pages', 'weight', 'dimensions',
                  'pub_date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор книги'
            }),
            "translator": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Переводчик'
            }),
            "publishing": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Издательство'
            }),
            "series": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия'
            }),
            "genre": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр книги',
            }),
            "years": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возрастное ограничение'
            }),
            "rating": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Популярность книги'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание книги'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            }),
            "pages": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страницы'
            }),
            "weight": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Масса'
            }),
            "dimensions": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Размеры'
            }),
            "pub_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации книги'
            }),
        }
