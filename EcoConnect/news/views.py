from django.shortcuts import get_object_or_404, render
from .models import News

# Create your views here.
app_name = "news"
def news_list(request):
    news_articles = News.objects.all().order_by('-date')  # latest first
    return render(request, 'news_list.html', {'news_articles': news_articles})

def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news_detail.html', {'news_item': news_item})