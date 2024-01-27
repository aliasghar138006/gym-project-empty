from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request ,"home_module/index.html" , {})

def product_page_view(request):
    return render(request ,"home_module/product.html" , {})

def signup_page_view(request):
    return render(request ,"home_module/signup.html" , {})

def login_type_view(request):
    return render(request ,"home_module/signin.html" , {})

def login_page_view(request):
    return render(request ,"home_module/login.html" , {})
