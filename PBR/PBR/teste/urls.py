from django.conf.urls import url, include
from django.contrib import admin
from core.views import bilhetef

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'formulario/$', bilhetef, name ='bilhetef'),
]
