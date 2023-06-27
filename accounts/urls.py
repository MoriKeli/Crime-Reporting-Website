from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UsersLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('officials/profile/', views.OfficialsProfileView.as_view(), name='officials_profile'),
    path('profile/', views.UsersProfileView.as_view(), name='user_profile'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]