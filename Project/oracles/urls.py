from django.urls import path

from . import views

app_name = 'oracles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('category/<str:category>/', views.category, name='category'),
    path('category/', views.indexCategory, name='indexCategory')
]