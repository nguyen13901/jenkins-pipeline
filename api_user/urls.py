from django.urls import path
from . import views
app_name = 'api_user'
urlpatterns = [
    path('', views.index, name='index'),
]