from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path(r'hello/', views.say_hello),
]