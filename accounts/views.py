from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import SignupForm, UpdateOfficersProfileForm, UpdateUserProfileForm

class UsersLoginView(View):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'LoginForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user_account = authenticate(username=username, password=password)

            if user_account is not None:
                if user_account.is_officer is False:
                    if user_account.is_registered:  # if the user (normal user) is registered, redirect to homepage.
                            return redirect('homepage')
                        
                    else:   # redirect to user's profile page if user (normal user) is not registered.
                        login(request, user_account)
                        return redirect('user_profile')
                    
                else:
                    # if the officer is not registered redirect to officer profile page
                    if user_account.is_officer is False and user_account.officerprofile.is_registered is False:
                        login(request, user_account)
                        return redirect('officials_profile')
                    
                    if user_account.officerprofile.is_registered is True:      # check if the user is a registered officer
                        if user_account.is_officer is True:
                            login(request, user_account)
                            return redirect('dashboard')

        return render(request, self.template_name)

class SignupView(View):
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'SignupForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('user_profile')

        return render(request, self.template_name)

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_officer is True), name='get')  
class OfficialsProfileView(View):
    form_class = UpdateOfficersProfileForm
    template_name = 'officials/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user.officerprofile)

        context = {'UpdateOfficialForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.officerprofile)

        if form.is_valid():
            register_officer = form.save(commit=False)
            register_officer.is_registered = True
            register_officer.name.is_officer = True
            register_officer.save()

            messages.info(request, 'Profile successfully updated!')
            return redirect('officials_profile')

        return render(request, self.template_name)

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_officer is False), name='get')  
class UsersProfileView(View):
    form_class = UpdateUserProfileForm
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)

        context = {'UpdateUserForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            register_user = form.save(commit=False)
            register_user.is_registered = True
            register_user.save()

            messages.info(request, "You've successfully updated your profile!")
            return redirect('user_profile')

        return render(request, self.template_name)

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
