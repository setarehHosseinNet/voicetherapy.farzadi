from django.contrib import messages
from Home.form import *
# from Home.models import *
from django.shortcuts import render, get_object_or_404, redirect
from Home.models import Article


# from .tables import ProductTable
# Create your views here.
def home_page(request):
    return render(request, 'Home/index.html')


def article(request):
    return render(request, 'Home/article.html')


def article_write(request):
    if request.method == "POST":
        form = ArticleWriteForm(request.POST)
        if form.is_valid():
            article_1 = form.save(commit=False)
            article_1.save()
            messages.success(request, 'You are now logged in', 'primary')
            return redirect('home1:Article_list')
    else:
        return render(request, 'Home/article_write.html', {'form': ArticleWriteForm()})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'Home/Article_list.html', {'articles': articles})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home1:Article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'home/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home1:article_list')
    return render(request, 'home/article_confirm_delete.html', {'article': article})


def article_Section(request):
    articles = Article.objects.all()
    return render(request, 'Home/Article_section.html', {'articles': articles})