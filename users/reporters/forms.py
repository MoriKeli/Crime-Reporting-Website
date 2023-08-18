from .utils import validate_file_type
from .models import CrimeRecords
from django import forms

class ReportCrimesForm(forms.ModelForm):
    SELECT_TYPE_OF_CRIME = (
        (None, '-- Select type of crime --'),
        ('Drug trafficking', 'Drug trafficking'),
        ('Human trafficking/kidnap', 'Human trafficking/kidnap'),
        ('Robbery', 'Robbery'),
        ('Sexual assault', 'Sexual assault'),
        ('Terrorism', 'Terrorism'),
        ('Theft', 'Theft'),
    )

    description = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text', 'placeholder': 'Explain the crime in details ...', 'class': 'mb-2',
    }))
    dt_crime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'date', 'class': 'mb-2',
    }))
    county = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mb-2',
    }))
    sub_county = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mb-2',
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mb-2',
    }))
    type_of_crime = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mb-2',
    }))
    file = forms.FileField(widget=forms.FileInput(attrs={
        'type': 'file', 'class': 'form-control', 'accept': '.3gp, .gif, .jpeg, .jpg, .mp3, .mp4, .ogg'
        }),
        validators=[validate_file_type],
    )
    
    class Meta:
        model = CrimeRecords
        fields = '__all__'