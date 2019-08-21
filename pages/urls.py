from django.urls import path
from . import views

urlpatterns = [
    path('num/push/', views.num_push),
    path('num/pull/', views.num_pull),
    path('static_example/', views.static_example),
    path('api_lotto/', views.api_lotto),
    path('api_lotto_result/', views.api_lotto_result),
    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('result/', views.result),
    path('search/', views.search),
    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('index/', views.index),
    path('introduce/', views.introduce),
]   