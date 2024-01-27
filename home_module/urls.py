from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home_page_view),
    path('product/' , views.product_page_view),
    path('signup/' , views.signup_page_view),
    path('login/' , views.login_page_view)
]