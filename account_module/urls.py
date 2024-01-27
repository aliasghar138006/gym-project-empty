from django.urls import path
from . import views

urlpatterns = [
    path('gymmanager/' , views.gymmanager_account_view),
    path('bodybuilder/' , views.bodybuilder_account_view),
    path('coach/' , views.coach_account_view),
    path('crew/' , views.crew_account_view),
    path('damage/' , views.damage_form_view),
    path('worktime/' , views.worktime_form_view),
    path('movement/' , views.movement_form_view)
]