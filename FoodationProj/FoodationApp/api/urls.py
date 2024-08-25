from django.urls import path
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('food/signup/', SignupView.as_view(), name='signup'),
    path('food/login/', LoginView.as_view(), name='login'),
    path('food/logout/', LogoutView.as_view(), name='logout'),
]
