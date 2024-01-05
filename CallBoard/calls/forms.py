from django import forms
from .models import Call, Respond


class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = [
            'call_category',
            'call_header',
            'call_text',
            'call_img',
        ]


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = [
            'respond_text',
        ]


