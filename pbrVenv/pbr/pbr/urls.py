from django.conf.urls import url, include
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'formulario/$', views.bilhetef, name ='bilhetef'),
    url(r'lista/$',views.lista, name='lista'),


]
