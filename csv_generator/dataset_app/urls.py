from django.urls import path

from . import views


urlpatterns = [
    path('schemas/', views.SchemaListView.as_view(), name='schemas-list'),
    path('schemas/create/', views.schema_create, name='schema-create'),
    path('schemas/update/<int:pk>/', views.schema_update, name='schema-update'),
    path('schemas/delete/<int:pk>/', views.schema_delete, name='schema-delete'),

    path('delete-column/<int:pk>/', views.column_delete, name='column-delete'),

    path('schema/<int:pk>/datasets/', views.dataset_list, name='dataset-list'),
    path('schema/<int:pk>/csv-generate/', views.generate_csv, name='csv-generate'),
    path('schema/<int:pk>/csv-download/', views.download_csv, name='csv-download'),
]
