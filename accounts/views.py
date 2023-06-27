from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import SignupForm, UpdateOfficialProfileForm

class UsersLoginView(View):
    form_class = AuthenticationForm
    template_name = 'dashboard/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'LoginForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):

        return render(request, self.template_name)

class SignupView(View):
    form_class = SignupForm
    template_name = 'dashboard/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'SignupForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        return render(request, self.template_name)
    
class UpdateOfficialsProfileView(View):
    form_class = UpdateOfficialProfileForm
    template_name = 'dashboard/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user.officialsprofile)

        context = {'UpdateOfficialForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.officialsprofile)

        return render(request, self.template_name)

class LogoutUser(LogoutView):
    template_name = 'dashboard/logout.html'
