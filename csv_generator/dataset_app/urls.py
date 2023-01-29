from django.urls import path
from . import views


urlpatterns = [
    path('schemas/', views.schemas_list, name='schemas-list'),
]
