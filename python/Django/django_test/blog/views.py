from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  # 导入Article模型

def hello_world(request):
    return HttpResponse("Hello World")

def article_content(request):
    # 获取第一篇文章，如果没有文章，则返回None
    article = Article.objects.first()

    if article is not None:
        title = article.title
        brief_content = article.brief_content  # 使用正确的字段名
        article_id = article.article_id
        publish_date = article.publish_date

        # 构建返回的字符串
        return_str = f'Title: {title}<br>' \
                     f'Brief Content: {brief_content}<br>' \
                     f'Article ID: {article_id}<br>' \
                     f'Publish Date: {publish_date}<br>'

        return HttpResponse(return_str, content_type='text/html')
    else:
        return HttpResponse("No articles found.", content_type='text/html')