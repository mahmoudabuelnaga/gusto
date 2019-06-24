from django.urls import path
from . import views 

urlpatterns = [
    path('', views.gusto, name='gusto'),
    # path('contact/', views.contact, name='contact'),
]