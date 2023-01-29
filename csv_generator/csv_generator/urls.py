from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('accounts/', include('user_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dataset_app.urls')),
]
