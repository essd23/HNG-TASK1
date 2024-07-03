from django.urls import path
from hello_api import views

urlpatterns = [
    path('api/hello/', views.hello_api, name='hello_api'),



]