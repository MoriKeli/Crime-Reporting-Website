from .models import PolicePosts, SuspectsRecords
from .utils import validate_is_image
from django import forms


class FileSuspectsForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_TYPE_OF_CRIME = (
        (None, '-- Select type of crime --'),
        ('Drug trafficking', 'Drug trafficking'),
        ('HT/Kidnap', 'Human trafficking/kidnap'),
        ('Robbery', 'Robbery'),
        ('Sexual assault', 'Sexual assault'),
        ('Terrorism', 'Terrorism'),
        ('Theft', 'Theft'),
    )
    SELECT_COUNTY = (
        (None, '-- Select county of origin --'),
        ('County 1', 'County 1'),
        ('County 2', 'County 2'),
        ('County 3', 'County 3'),
    )
    SELECT_SUB_COUNTY = (
        (None, '-- Select sub-county of origin --'),
        ('Sub-county 1', 'Sub-county 1'),
        ('Sub-county 2', 'Sub-county 2'),
        ('Sub-county 3', 'Sub-county 3'),
    )
    SELECT_CONSTITUENCY = (
        (None, '-- Select constituency of origin --'),
        ('Constituency 1', 'Constituency 1'),
        ('Constituency 2', 'Constituency 2'),
        ('Constituency 3', 'Constituency 3'),
    )
    SELECT_LOCATION = (
        (None, '-- Select location of origin --'),
        ('Location 1', 'Location 1'),
        ('Location 2', 'Location 2'),
        ('Location 3', 'Location 3'),
    )
    SELECT_SUSPECT_STATUS = (
        (None, '-- Select suspect status --'),
        ('Arrested', 'Arrested'),
        ('Detained', 'Detained'),
        ('Hiding', 'Hiding'),
        ('Jailed', 'Jailed'),
        ('Wanted', 'Wanted'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
    }),
    help_text='Enter the full name (i.e. first name, middle name and surname) of the suspect'
    )
    alias = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mt-2',
        }),
        help_text='Enter the alias of the suspect, e.g. <b>"black widow", "masha" or "yule msee", etc.</b>',
        required=True,
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mt-2 mb-2',
        }),
        choices=SELECT_GENDER,
    )
    county_origin = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select',
        }),
        choices=SELECT_COUNTY,
        help_text='Enter the county of origin of the suspect',
    )
    subcounty_origin = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mt-2',
        }),
        choices=SELECT_SUB_COUNTY,
        help_text='Enter the sub-county of origin of the suspect',
    )
    constituency_origin = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mt-2',
        }),
        choices=SELECT_CONSTITUENCY,
        help_text='Enter the constituency of origin of the suspect',
    )
    location_origin = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mt-2',
        }),
        choices=SELECT_LOCATION,
        help_text='Enter the location of origin of the suspect',
    )
    bounty = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'number', 'class': 'mt-2 mb-2',
    }))
    crime = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'text', 'class': 'mt-2',
        }),
        choices=SELECT_TYPE_OF_CRIME,
    )
    status = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'text', 'class': 'mt-2',
        }),
        choices=SELECT_SUSPECT_STATUS,
    )
    last_seen_county = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'text', 'class': 'mt-2',
        }),
        choices=SELECT_COUNTY,
    )
    last_seen_location = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'text', 'class': 'mt-2',
        }),
        choices=SELECT_LOCATION,
    )
    suspect_dp = forms.FileField(widget=forms.FileInput(attrs={
        'type': 'file', 'accept': '.jpg, .jpeg, .png',
        }),
        validators=[validate_is_image],
    )
    

    class Meta:
        model = SuspectsRecords
        fields = '__all__'