from django.urls import path
from users import views


urlpatterns = [
    path('', views.user_login_view, name='user_login'),
    path('create-user-account/', views.signup_user, name='signup'),
    path('homepage/<str:name>/', views.homepage, name='user_homepage'),
    path('edit-my-profile/', views.user_profile, name='user_profile'),
    path('about-us/', views.about_us, name='about'),
    path('users/reporta-crime/', views.report_crime_view, name='report_crime'),
    path('crime-details/<str:pk>/', views.crime_details_view, name='crime_details'),
    path('reported-crimes/', views.crime_reports_view, name='crime_reports'),
    path('most-wanted-suspects/', views.most_wanted_view, name='wanted'),
    path('wanted-suspect-details/<str:name>/wanted/<int:bounty>/report/', views.suspect_info_view, name='suspect_info'),
    path('registered-users/summary-of-individual-crime-reports/', views.individual_crime_reports_view, name='summary'),
    path('contact-us/', views.contact_us_view, name='contact'),
    
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]