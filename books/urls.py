from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_home, name='books_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BooksDetailView.as_view(), name='books-detail'),
]
