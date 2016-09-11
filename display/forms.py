from django import forms
# from .models import Assets


class Asset(forms.Form):
    gdzc = forms.CharField()
