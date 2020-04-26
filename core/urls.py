from django.urls import path
from .utils import *

from .views import RegisterView, LoginView, LogoutView,DashboardView

urlpatterns = [
   
    path('login/', LoginView.as_view(), name='login-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('is_upvoted/<answer>',is_upvoted,name='is_upvoted'),
]