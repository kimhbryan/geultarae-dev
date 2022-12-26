from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask, name='ask'),
    path('mypage/', views.mypage, name='mypage'),
    path('writing1/', views.writing1, name='writing1'),
    path('writing2/', views.writing2, name='writing2'),
]
