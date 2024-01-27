from django.shortcuts import render

# Create your views here.

def gymmanager_account_view(request):
    return render(request , "account_module/gymmanager.html" , {})

def bodybuilder_account_view(request):
    return render(request , "account_module/bodybuilder.html" , {})

def coach_account_view(request):
    return render(request , "account_module/coach.html" , {})

def crew_account_view(request):
    return render(request , "account_module/crew.html" , {})

def damage_form_view(request):
    return render(request , "account_module/forms/damage.html" , {})

def worktime_form_view(request):
    return render(request , "account_module/forms/worktime.html" , {})

def movement_form_view(request):
    return render(request , "account_module/forms/movement.html" , {})
