from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def books_home(request):
    books = Articles.objects.order_by()
    return render(request, 'books_home.html', {'books': books})


class BooksDetailView(DetailView):
    model = Articles
    template_name = "details_view.html"
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books_home")
        else:
            error = "Ошибка!"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create.html', data)
