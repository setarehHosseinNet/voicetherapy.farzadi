from django.urls import path

from . import views

app_name = 'home1'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('article', views.article, name='article'),
    path('article_write', views.article_write, name='article_write'),
    path('Article_List', views.article_list, name='Article_list'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),

]