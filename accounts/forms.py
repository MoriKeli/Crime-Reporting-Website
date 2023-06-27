from django.contrib.auth.forms import UserCreationForm
from .models import User, OfficialsProfile, UsersProfile
from django import forms

class SignupForm(UserCreationForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
                'type': 'text',
                'class': 'mb-2',
                'autofocus': True,
        }),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
                'type': 'text', 'class': 'mb-2',
        }),
        required=True)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
                'type': 'email', 'class': 'mb-2',
        }),
        required=True)
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={
                'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_GENDER
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'mb-2',
        }),
        required=True,
    )
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-2',
        }),
        required=True,
    )
    county = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        help_text='Enter your residential county',
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        help_text='Enter your residential location',
    )
    town = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        help_text='Enter the residential your estate/village/town.',
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'dob', 'phone_no', 'profile_pic',
        ]


class UpdateProfile(forms.ModelForm):
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-2',
        }),
        required=True,
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            'dob', 'profile_pic',
        ]
    
class UpdateOfficialProfileForm(forms.ModelForm):
    SELECT_RANK = (
        (None, '-- Select police rank --'),
        ('AP', 'Administration Police (AP)'),
        ('Chief', 'Chief'),
        ('Detective', 'Detective'),
        ('Police officer', 'Police officer'),
        ('Traffic police', 'Traffic police'),
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-2', 'placeholder': 'Type your bio here ...',
        }),
        required=False,
    )
    police_post = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
    )
    rank = forms.ChoiceField(
        widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_RANK,
    )
    county = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        help_text='Enter the county of your police post'
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        help_text='Enter the county of your police post'
    )
    town = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        help_text='Enter the estate/town/village of your police post',
    )
    phone_no_1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-2',
        }),
        required=True,
    )
    phone_no_2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-2',
        }),
        required=True,
    )
    phone_no_3 = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-2',
        }),
        required=True,
    )

    class Meta:
        model = OfficialsProfile
        fields = '__all__'

