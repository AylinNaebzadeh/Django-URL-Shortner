
from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirector_view, name="urlshortner"),
    path('final/<str:sh_url>' , views.final , name="final"),
]