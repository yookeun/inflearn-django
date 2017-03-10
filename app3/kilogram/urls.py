from django.conf.urls import url, include
from . import views

app_name = 'kilogram'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
]
