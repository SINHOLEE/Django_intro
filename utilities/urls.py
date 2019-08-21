from django.urls import path
from . import views

# utilities 로 왔을 때 이후에 온 url들이 뒤로 옴 => /utilities/___
urlpatterns = [
    path('index/', views.index),
]