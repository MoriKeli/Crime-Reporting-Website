from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ReportCrimesForm

class ReportCrimesView(View):
    form_class = ReportCrimesForm
    template_name = 'reporters/report.html'

    def get(self, request, user, *args, **kwargs):
        form = self.form_class()

        context = {}
        return render(request, self.template_name, context)
    
    def post(self, request, user, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.reported_by = request.user
            new_record.save()

            messages.success(request, 'Report successfully submitted!')
            return redirect('report_crime')
    
