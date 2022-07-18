from django.urls import path
from officers import views

urlpatterns = [
    path('', views.OfficerLogin.as_view(), name='official_login'),
    path('signup-officer/', views.signup_officer, name='official_signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('officer/edit-profile/', views.my_profile, name='my_profile'),
    path('reported-crime/<str:pk>/crimes/<str:report_id>/', views.file_case, name='file_reported_crime'),
    path('case-file-no/<str:file_no>/suspect/<str:suspect>/', views.view_case_file, name='case_file'),
    path('reported-crimes/', views.reported_crimes, name='reported_crimes'),
    path('filed-cases/', views.view_filed_cases, name='filed_cases'),
    path('case-filing-pending/', views.view_unfiled_cases, name='unfiled_cases'),
    path('wanted-suspects/', views.display_wanted_suspects, name='wanted_suspects'),
    path('police-occurence-book/<str:p_station>/', views.police_occurence_book, name='ob'),
    
    path('logout/', views.LogoutOfficer.as_view(), name='logout_officer'),    
]