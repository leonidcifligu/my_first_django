from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('bear/<str:name>/<int:age>/poke',views.bear),
]