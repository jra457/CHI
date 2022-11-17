from django import forms
from django.forms import ModelForm
from.models import packagesPerHour


class PackagesForm(ModelForm):
    class Meta:
        model = packagesPerHour
        #fields = "__all__"
        fields = ('location', 'pph', 'date')