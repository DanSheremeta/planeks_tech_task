from django.urls import path
from . import views


urlpatterns = [
    path('schemas/', views.schemas_list, name='schemas-list'),
    path('schemas/create/', views.schema_create, name='schema-create'),
    path('schemas/delete/<int:pk>/', views.schema_delete, name='schema-delete'),

    path('schemas/<int:pk>/create-column/', views.schema_column_create, name='column-create'),
    path('delete-column/<int:pk>/', views.column_delete, name='column-delete'),

    path('schema/<int:pk>/csv-generate/', views.dataset_list, name='dataset-list'),
]
