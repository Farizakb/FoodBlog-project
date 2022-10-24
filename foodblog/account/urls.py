from django.urls import path
from . import views
from .views import UserLoginView ,UserRegisterView, ActiveAccountView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.user_profile, name='profile'),
    path('login',UserLoginView.as_view(), name='login'),
    path('register',UserRegisterView.as_view(), name='register'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('activate/<str:uidb64>/<str:token>/',ActiveAccountView.as_view(), name='activate'),
    
]
