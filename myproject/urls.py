"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#http://127.0.0.1 여기로 접속했을 때 myapp에 있는 views.py로 이동하게 하려면
#http://127.0.0.1/app/ 

#http://127.0.0.1/create/ create를 접속했을 때
#http://127.0.0.1/read/1/ read를 접속했을 때

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 화면으로 
    path('',include('myapp.urls'))
]

#http://127.0.0.1 여기로 접속했을 때 myapp에 있는 views.py로 이동하게 하려면