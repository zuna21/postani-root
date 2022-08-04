from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Article, Category
from .forms import ArticleForm
from .utils import searchArticles, searchInCategory, paginationArticles

# Create your views here.

def articles(request):
    articles, search_query = searchArticles(request)
    custom_range, articles, paginator = paginationArticles(request, articles, 8)
    

    context = {
        'articles': articles,
        'search_query': search_query,
        'paginator': paginator,
        'custom_range': custom_range
    }

    return render(request, 'articles/articles.html', context)



def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'articles/article.html', context)


@login_required(login_url='articles')
def createArticle(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles')

    context = {'form': form}
    return render(request, 'articles/create-article.html', context)


def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'articles/categories.html', context)


def category(request, pk):
    articles, search_query = searchInCategory(request, pk)
    custom_range, articles, paginator = paginationArticles(request, articles, 8)

    context = {
        'articles': articles,
        'search_query': search_query,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'articles/category.html', context)



def about(request):
    return render(request, 'articles/about.html')