from django import forms
from .models import UserData
from django.forms import DateTimeInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = [
            'name',
            'surname',
            'gender',
            'birth_date'
        ]
        widgets = {
            'birth_date': DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'})
        }

