from django.urls import path
from . import views

# URLs for our pages
urlpatterns = [
    path('', views.index, name="index"),
    path('newUser/', views.newUser, name="newUser"),
    path('confirmedUser/', views.confirmedUser, name="confirmedUser"),
]
