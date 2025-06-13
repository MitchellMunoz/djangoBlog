from django.urls import path
from . import views

app_name = "receipts"

urlpatterns = [
    path("", views.list_receipt,  name="list"),   # /receipts/
    path("upload/", views.upload_receipt, name="upload"), # /receipts/upload/
]
