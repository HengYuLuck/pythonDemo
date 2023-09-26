from django.urls import path
import blog.views

urlpatterns = [
    path('hello_world/', blog.views.hello_world),  # 添加斜杠
    path('content/', blog.views.article_content),  # 添加斜杠
    path('index/', blog.views.get_index_page),  # 添加斜杠
    path('detail/<int:article_id>', blog.views.get_detail_page),  # 添加斜杠并添加新的别名
]
