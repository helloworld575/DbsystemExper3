"""Exper3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^main/', views.main_page, name='main'),
    url(r'^sql_search$',views.sql_search_page,name='sql_search'),
    url(r'^idef1x_show$',views.idef1x_show,name='idef1x_show'),
    url(r'^get_sql$',views.get_sql,name='get_sql'),
    url(r'^select_search$',views.select_search_page,name='select_search'),
    url(r'^get_sel$',views.select_search,name='get_sel')
]
