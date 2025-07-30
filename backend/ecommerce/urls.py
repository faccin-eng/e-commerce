from django.urls import path
from ecommerce import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("perfil/", views.perfil, name="perfil"),
]