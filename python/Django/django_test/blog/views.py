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

def get_index_page (request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                  {
                      'article_list': all_article
                  }
                  )

def get_detail_page (request, article_id):
    all_article = Article.objects.all()
    cur_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            cur_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = cur_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'cur_article': cur_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article
                  }
                  )