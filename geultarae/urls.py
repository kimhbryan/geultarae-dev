from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask, name='ask'),
    path('ask/done/', views.ask_done, name='ask_done'),
    path('mypage/', views.mypage, name='mypage'),
    path('writing/<int:pk>/', views.writing, name='writing'),
    path('plot/<int:pk>/', views.plot, name='plot')
]
