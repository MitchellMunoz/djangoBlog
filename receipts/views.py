# receipts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
                                                 #     (.objects lives here)
def upload_receipt(request):

    return render(request, "receipts/upload.html")
def list_receipt(request):

    return render(request, "receipts/list.html")
