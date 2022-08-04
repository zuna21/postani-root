from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article, Category

def searchArticles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    categories = Category.objects.filter(title__icontains=search_query)
    articles = Article.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(category__in=categories)
    )

    return articles, search_query


def searchInCategory(request, pk):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    articles = Article.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query)
    )

    articles = articles.filter(category=pk)
    return articles, search_query


def paginationArticles(request, articles, results):
    page = request.GET.get('page')
    paginator = Paginator(articles, results)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        articles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        articles = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, articles, paginator