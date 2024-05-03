"""
URL configuration for NYHouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('addCSV/', views.addCSV),
    path('houseList/', views.house_list, name='houseList'),
    path('houseList/<int:page>/', views.house_list, name='house_list_by_page'),
    path('houseList/add/', views.house_list_add),
    path('houseList/<str:nid>/<str:sid>/edit/', views.house_list_edit),
    path('houseList/<str:nid>/<str:sid>/delete/', views.house_delete),
    path('houseListUser/', views.houseListUser,name='houseListUser'),
    path('houseListUser/<int:page>/', views.houseListUser, name='house_list_user_by_page'),
]
