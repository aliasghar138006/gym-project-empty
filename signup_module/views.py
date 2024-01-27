from django.shortcuts import render

# Create your views here.



def signup_bodybuilder_page_view(request):
    return render(request , "signup_module/bodybuilder.html" , {})


def signup_coach_page_view(request):
    return render(request , "signup_module/coach.html" , {})

def signup_crew_page_view(request):
    return render(request , "signup_module/crew.html" , {})

def signup_gym_page_view(request):
    return render(request , "signup_module/gym.html" , {})
