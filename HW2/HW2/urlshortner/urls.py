
from django.urls import path
from .views import *

urlpatterns = [
    path('', url_shortner, name="urlshortner"),
]