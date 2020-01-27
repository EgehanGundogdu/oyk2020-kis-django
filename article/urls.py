from django.urls import path
from article.views import ArticleListView, ArticleCreateView, ArticleDetailView
urlpatterns = [
    path('', ArticleListView.as_view(), name='post_list'),
    path('create/', ArticleCreateView.as_view(), name='post_create'),
    path('detail/<int:post_id>/', ArticleDetailView.as_view(), name='post_detail'),
]
