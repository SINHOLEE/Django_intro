"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 경로를 잘 보라.
# pages/views.py/index()
# pages라는 어플리케이션안에 있는 view.py라는 파일을 임포트 해서, view.index 함수를 접근하도록 하자.

urlpatterns = [
	
    path('admin/', admin.site.urls),

    # django_intro/urls.py로 사용자의 요청이 들어오면, pages/urls.py로 보낸다는 제어문
    # import path, include
    path('pages/', include('pages.urls')),
    path('utilities/', include('utilities.urls')),
]
