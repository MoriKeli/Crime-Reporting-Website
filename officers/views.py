from datetime import datetime
from officers.forms import EditProfile, SignUpForm, UpdateProfile, CrimeStatusReportForm, PostWantedSuspectsStatus
from officers.models import CrimeReported, OfficialsProfile, WantedSuspect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

class OfficerLogin(LoginView):
    template_name = 'officers/login.html'


def signup_officer(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            reg_officer = form.save(commit=False)
            reg_officer.username = reg_officer.first_name + ' ' + reg_officer.last_name
            reg_officer.is_staff = True
            reg_officer.save()
            
            messages.success(request, f'Account for {reg_officer.username} created successfully!')
            return redirect('my_profile')
        
    context = {'signup_form': form}
    return render(request, 'officers/signup.html', context)


@login_required(login_url='official_login')
def homepage(request):
    crimes_reported = CrimeReported.objects.filter(location=request.user.officialsprofile.police_post).all()
    wanted_suspects = WantedSuspect.objects.filter().all()
    
    
    context = {
        'reported_crimes': crimes_reported, 'wanted_suspects': wanted_suspects,
        'reported_today': crimes_reported.filter(crime_reported__date=datetime.today().strftime("%Y-%m-%d")),
        
        'total_crimes': crimes_reported.count(),
        'filed_cases': CrimeReported.objects.filter(location=request.user.officialsprofile.police_post, crime_status__contains=' ', status_updated__date__contains=datetime.today().strftime("%m")).count(),
        'pending': CrimeReported.objects.filter(location=request.user.officialsprofile.police_post, crime_status='').count(),
        'total_suspects': wanted_suspects.count(),
        'total_officers': OfficialsProfile.objects.filter(police_post=request.user.officialsprofile.police_post, gender__contains='a').count()
        }
    return render(request, 'officers/homepage.html', context)


@login_required(login_url='official_login')
def my_profile(request):
    form = UpdateProfile(instance=request.user.officialsprofile)
    editprof_form = EditProfile(instance=request.user.officialsprofile)
    
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance=request.user.officialsprofile)
        editprof_form = EditProfile(request.POST, request.FILES, instance=request.user.officialsprofile)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
                    
        elif editprof_form.is_valid():
            editprof_form.save()
            messages.info(request, 'Profile edited succesfully!')
            
        return redirect('my_profile')
    
    context = {'updateProfile': form, 'editProfile': editprof_form}
    return render(request, 'officers/profile.html', context)

@login_required(login_url='official_login')
def file_case(request, pk, report_id):
    file_no = CrimeReported.objects.get(case_file_no=pk)
    report_id = file_no.suspect_name

    case_form = CrimeStatusReportForm(instance=file_no)
    suspects_form = PostWantedSuspectsStatus()
    
    if request.method == 'POST':
        case_form = CrimeStatusReportForm(request.POST, instance=file_no)
        suspects_form = PostWantedSuspectsStatus(request.POST, request.FILES)
        
        if case_form.is_valid():
            case_form.save()
            messages.success(request, 'Case updated successfully!')

        elif suspects_form.is_valid():
            suspects_form.save()
            messages.info(request, 'Suspect posted successfully.')
            
        return redirect('file_reported_crime', pk, report_id)
    
    context = {'case_form': case_form, 'wanted': suspects_form}
    return render(request, 'officers/file-case.html', context)


@login_required(login_url='official_login')
def reported_crimes(request):
    r_crimes = CrimeReported.objects.filter(location__contains=request.user.officialsprofile.police_post).all()
    
    context = {'reported_crimes': r_crimes}
    return render(request, 'officers/crimes.html', context)


@login_required(login_url='official_login')
def display_wanted_suspects(request):
    w_suspects = WantedSuspect.objects.filter().all()
    
    context = {'wanted': w_suspects}
    return render(request, 'officers/suspects.html', context)


@login_required(login_url='official_login')
def view_filed_cases(request):
    filed_cases = CrimeReported.objects.filter(crime_status='File Case').all()
    
    context = {'filed': filed_cases}
    return render(request, 'officers/filed.html', context)


@login_required(login_url='official_login')
def view_unfiled_cases(request):
    cases = CrimeReported.objects.filter(crime_status='').all()
    
    context = {'unfiled': cases}
    return render(request, 'officers/pending-cases.html', context)


@login_required(login_url='official_login')
def view_case_file(request, file_no, suspect):
    file_no = CrimeReported.objects.get(case_file_no=file_no)
    suspect = file_no.suspect_name
    
    
    context = {'suspect': suspect, 'file_no': file_no}
    return render(request, 'officers/case-details.html', context)


@login_required(login_url='official_login')
def police_occurence_book(request, p_station):
    police_station = OfficialsProfile.objects.get(police_post=p_station)
        
    
    context = {}
    return render(request, 'officers/ob.html', context)


class LogoutOfficer(LogoutView):
    template_name = 'officers/logout.html'