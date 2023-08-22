from .forms import FileSuspectsForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.officerprofile.is_registered is True), name='get')
class ReportedSuspectsView(View):
    form_class = FileSuspectsForm
    template_name = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.info(request, 'Form successfully submitted!')
            return redirect('')
        
        return render(request, self.template_name)

