from django.urls import path
from article.views import ArticleListView, ArticleDeleteView, ArticleCreateView, ArticleDetailView, ArticleUpdateView
urlpatterns = [
    path('', ArticleListView.as_view(), name='post_list'),
    path('create/', ArticleCreateView.as_view(), name='post_create'),
    path('detail/<int:post_id>/', ArticleDetailView.as_view(), name='post_detail'),
    path('update/<int:post_id>/', ArticleUpdateView.as_view(), name='post_update')
    ,path('delete/<int:post_id>/', ArticleDeleteView.as_view(), name='post_update')

]
