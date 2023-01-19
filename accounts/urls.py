from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from .views import UserRegisterView

urlpatterns = [

    # Management
    path('register/',UserRegisterView.as_view(),name='register'),
    # path(
    #     route='login/',
    #     view=views.LoginView.as_view(),
    #     name='login'
    # ),
]