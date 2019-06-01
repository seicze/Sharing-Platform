"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app01 import views,resource
from django.conf.urls import url,include

urlpatterns = [
    path('', views.register),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('registerView/', views.registerView),
    path('register/', views.register),
    path('login/', views.login),
    path('accounts/login/', views.logout),
    path(r'userinfoView/<int:user_id>/', views.userinfoView),
    #path('search/', views.search),
    path(r'search/', include('haystack.urls')),
    path(r'message/', views.message),
    path(r'essay/', resource.essayView),
    path('PS/',views.customerps),
    path('ExpertPS/',views.expertps),
    path('personalmodify/',views.personalmodify),
    path('personalchanged/',views.personalchange),
    path('recharge/',views.recharge),
    path(r'identify/',views.identify),
    path(r'confirmM/',views.confirmM),
    path(r'confirmI/',views.confirmI),
    path(r'confirminfo/', views.confirminfo),
    path(r'success/', views.success),
    path(r'expert/',views.expert),
    path(r'topup/',views.topup),
    path(r'hotspot',resource.hotspot),
    path(r'register',views.register),
]
