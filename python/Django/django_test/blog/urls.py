from django.urls import path
from blog import views  # 请根据实际项目结构调整导入路径

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),  # 注意斜杠
    path('content/', views.article_content, name='article_content'),  # 注意斜杠
]
