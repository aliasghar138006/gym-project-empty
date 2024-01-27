from django.shortcuts import render

# Create your views here.

def gymmanager_account_view(request):
    return render(request , "account_module/gymmanager.html" , {})
