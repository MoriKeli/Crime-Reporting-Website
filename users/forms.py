from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from officers.models import CrimeReported
from users.models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
class UpdateProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'mb-2'}), choices=((None, '-- Select gender --'), ('Male', 'Male'), ('Female', 'Female')))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), label='Date of Birth')
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'mb-2', 'placeholder': 'Enter your residence/location'}))
    
    class Meta:
        model = UserProfile
        fields = ['gender', 'dob', 'location']
        

class ReportCrimeForm(forms.ModelForm):
    choice_crime = (
        (None, '-- Select type of crime --'),
        ('Burglary', 'Burglary'),
        ('Robbery', 'Robbery'),
        ('Selling Drugs', 'Selling Drugs'),
        ('Sexual Assault', 'Sexual Assault'),
        ('Terrorism', 'Terrorism'),
        ('Theft', 'Theft'),
    )
    suspect_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter suspect(s) name'}),label='')
    type_of_crime = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), label='', 
                    help_text='<b>NB: </b>If the crime you are reporting involves drugs, hard drugs such as "bhang/marijuana", "cocaine", "heroin" will be considered illegal. If not your case will be discarded.', choices=choice_crime)
    location = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Where did the crime occur?'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Describe the crime in details...'}), 
                                  label='', help_text='Describe the crime in details. Please mention the victims involved')
    
    date_of_crime = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}), label='')
    
    class Meta:
        model = CrimeReported
        fields = ['suspect_name', 'type_of_crime', 'location', 'description', 'date_of_crime']
        
