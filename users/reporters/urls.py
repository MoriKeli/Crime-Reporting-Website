from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>/report/crimes/', views.ReportCrimesView.as_view(), name='report_crime'),
    
]