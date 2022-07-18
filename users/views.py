from datetime import datetime
from turtle import update
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from officers.models import CrimeReported, WantedSuspect
from users.utils import get_plot
from users.forms import ReportCrimeForm, SignUpForm, UpdateProfileForm
from users.models import UserProfile
import uuid

def user_login_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        
        user = auth.authenticate(username=user_name, password=user_password)
        
        if user is not None and user.is_staff is False:
            auth.login(request, user)
            return redirect('user_homepage', user.username)
        
        else:
            messages.error(request, 'Invalid Credentials. Username and password may be case-sensitive')
            
        return redirect('user_login')        
    return render(request, 'users/index.html')

def signup_user(request):
    signup_form = SignUpForm()
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        
        if signup_form.is_valid():
            signin = signup_form.save(commit=False)
            signin.username = signin.first_name + ' ' + signin.last_name
            signin.staff = False
            signin.save()
            messages.success(request, 'Account created successfully!')
        
        return redirect('user_profile')
    context = {'form': signup_form}
    return render(request, 'users/signup.html', context)


@login_required(login_url='user_login')
def homepage(request, name):
    logged_in_user = User.objects.get(username=name)
    reported_crimes = CrimeReported.objects.filter().all()
    
    context = {'reported_crimes': reported_crimes}
    return render(request, 'users/homepage.html', context)


@login_required(login_url='user_login')
def user_profile(request):
    profile_form = UpdateProfileForm(instance=request.user.userprofile)
    
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            
            messages.info(request, 'Your profile has been updated successfully.')
            return redirect('user_homepage', request.user.username)
    
    context = {'update_profile': profile_form}
    return render(request, 'users/profile.html', context)


@login_required(login_url='user_login')
def about_us(request):
    
    return render(request, 'users/about.html')


@login_required(login_url='user_login')
def report_crime_view(request):
    report_form = ReportCrimeForm()
    
    if request.method == 'POST':
        report_form = ReportCrimeForm(request.POST)
        
        if report_form.is_valid():
            crime = report_form.save(commit=False)
            crime.reported_by = request.user.username
            crime.save()
            
            messages.success(request, 'Report submitted successfully')
            return redirect('report_crime')
    
    context = {'ReportCrimeForm': report_form}
    return render(request, 'users/report-crime.html', context)


@login_required(login_url='user_login')
def crime_reports_view(request):
    reported_crimes = CrimeReported.objects.filter(location=request.user.userprofile.location).all().order_by('crime_reported')
    crime_updates = CrimeReported.objects.filter(location=request.user.userprofile.location).all().order_by('status_updated')
    
    context = {'crimes_reported': reported_crimes, 'crime_report_updates': crime_updates}
    return render(request, 'users/crime-reports.html', context)


@login_required(login_url='user_login')
def crime_details_view(request, pk):
    crime_d = CrimeReported.objects.get(case_file_no=pk)
    
    context = {'crime_details': crime_d}
    return render(request, 'users/crime-details.html', context)


@login_required(login_url='user_login')
def contact_us_view(request):
    
    return render(request, 'users/contact.html')


@login_required(login_url='user_login')
def most_wanted_view(request):
    suspect = WantedSuspect.objects.filter().all().order_by('bounty')

    context = {'wanted_suspects': suspect}
    return render(request, 'users/most-wanted.html', context)


@login_required(login_url='user_login')
def suspect_info_view(request, name, bounty):
    suspect = WantedSuspect.objects.get(id=name)
    bounty = suspect.bounty
    
    context = {'info': suspect}
    return render(request, 'users/suspect-details.html', context)


@login_required(login_url='user_login')
def individual_crime_reports_view(request):
    crime_reports = CrimeReported.objects.filter(reported_by=request.user.username).order_by('crime_reported')
    
    context = {'crime_report_summary': crime_reports}
    return render(request, 'users/summary.html', context)

class LogoutUser(LogoutView):
    template_name = 'users/logout.html'
    
