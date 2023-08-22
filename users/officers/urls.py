from . import views
from django.urls import path

urlpatterns = [
    path('suspect/new/', views.ReportedSuspectsView.as_view(), name='new_suspect'),

]