from django.urls import path, include

from apps.views import hello_world

urlpatterns = [
    path('hello',  hello_world)
]
