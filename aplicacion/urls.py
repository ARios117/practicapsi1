from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^usuario/$', views.lista_usuarios, name='lista_usuarios'),
]
