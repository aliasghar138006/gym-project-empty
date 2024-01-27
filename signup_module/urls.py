from django.urls import path
from . import views

urlpatterns = [
    path('body-builder/' , views.signup_bodybuilder_page_view),
    path('coach/' , views.signup_coach_page_view),
    path('crew/' , views.signup_crew_page_view),
    path('gym/' , views.signup_gym_page_view)
]