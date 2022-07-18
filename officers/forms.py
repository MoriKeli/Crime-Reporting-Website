from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from officers.models import OfficialsProfile, CrimeReported, WantedSuspect


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
        
class UpdateProfile(forms.ModelForm):
    choice_rank = (
        (None, '--- Select your rank ---'),
        ('Inspector General', 'Inspector General'),
        ('Deputy Inspector General', 'Deputy Inspector General'),
        ('Senior Assistant Inspector General', 'Senior Assistant Inspector General'),
        ('Assistant Inspector General', 'Assistant Inspector General'),
        ('Commissioner', 'Commissioner'),
        ('Senior Superintendent', 'Senior Superintendent'),
        ('Superintendent of Police', 'Superintendent of Police'),
        ('Assistant Superintendent', 'Assistant Superintendent'),
        ('Chief Inspector', 'Chief Inspector'),
        ('Inspector', 'Inspector'),
        ('Senior Sergeant', 'Senior Sergeant'),
        ('Sergeant', 'Sergeant'),
        ('Corporal', 'Corporal'),        
    )
    
    officer_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter officer_id', 'type': 'text', 'class': 'mt-2'}), label='')
    police_post = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your police_post', 'type': 'text', 'class': 'mt-2'}), label='')
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), label='', choices=(('Male', 'Male'), ('Female', 'Female')))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mt-2'}), label='')
    rank = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2 mb-2'}), choices=choice_rank, label='')
    dp = forms.ImageField(widget=forms.FileInput(attrs={'class': 'mt-1'}), label='Your passport(image)', required=True)
    
    class Meta:
        model = OfficialsProfile
        fields = ['gender', 'dob', 'phone_no', 'officer_no', 'police_post', 'rank', 'dp']


class EditProfile(forms.ModelForm):
    police_post = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2 mb-2'}))
    dp = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'mt-1'}), label='Your passport(image)')
    
    class Meta:
        model = OfficialsProfile
        fields = ['police_post', 'dp']


class CrimeStatusReportForm(forms.ModelForm):
    crime_choice = (
        (None, '-- Select case status --'),
        ('File Case', 'File Case'),
        ('Police carrying out investigation', 'Police carrying out investigation'),
        ('Suspect(s) Arrested', 'Suspect(s) Arrested'),
        ('Suspect(s) Interrogated', 'Suspect(s) Interrogated'),
        ('Suspect(s) Sentenced', 'Suspect(s) Sentenced'),
        ('Case closed', 'Case closed'),
    )

    suspect_name = forms.CharField(disabled=True, label='Suspect Name', widget=forms.TextInput(attrs={'class': 'mb-2', 'type': 'text'}))
    type_of_crime = forms.CharField(disabled=True, label='Crime', widget=forms.TextInput(attrs={'class': 'mb-2', 'type': 'text'}))
    location = forms.CharField(disabled=True, label='Crime Location', widget=forms.TextInput(attrs={'class': 'mb-2', 'type': 'text'}))
    description = forms.CharField(disabled=True, label='Description', widget=forms.Textarea(attrs={'class': 'mb-2'}))
    crime_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=crime_choice, label='Crime Status')    
    
    class Meta:
        model = CrimeReported
        fields = ['suspect_name', 'type_of_crime', 'location', 'description', 'crime_status']
        

class PostWantedSuspectsStatus(forms.ModelForm):
    suspect_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter suspect name ...', 'class': 'mb-2'}), label='', required=True)
    alias = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter alias name ...(Optional)', 'class': 'mb-2'}), label='', required=False)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', required=True, choices=((None, '--Select gender --'), ('Male', 'Male'), ('Female', 'Female')))
    crime = forms.CharField(widget=forms.TextInput(attrs={'type': 'select', 'class': 'mb-2', 'placeholder': 'Enter crime committed by suspect'}), label='', required=True)
    bounty = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2', 'placeholder': 'Enter bounty in Kshs.', 'min': '0'}), label='', required=True)
    last_seen = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Where was the suspect last seen?', 'class': 'mb-2'}), label='', required=True)
    suspect_pic = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'mt-1 mb-2'}), label='Image of the suspect')
    status = forms.ChoiceField(required=True, label='', choices=((None, '--- Select suspect status ---'), ('Hiding', 'Hiding'), ('Apprehended', 'Apprehended'), ('Murdered', 'Murdered')))
    
    class Meta:
        model = WantedSuspect
        fields = ['suspect_name', 'alias', 'gender', 'crime', 'bounty', 'last_seen', 'status', 'suspect_pic']
