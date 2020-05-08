from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
]