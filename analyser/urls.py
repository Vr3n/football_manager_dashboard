from django.urls import path

from .views import index, upload_squad

urlpatterns = [
    path('', index, name="index"),
    path('upload-squad/', upload_squad, name="upload-squad"),
]
