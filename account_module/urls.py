from django.urls import path
from . import views

urlpatterns = [
    path('gymmanager/' , views.gymmanager_account_view)
]