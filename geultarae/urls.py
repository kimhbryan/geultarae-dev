from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask, name='ask'),
    path('mypage/', views.mypage, name='mypage'),
]
