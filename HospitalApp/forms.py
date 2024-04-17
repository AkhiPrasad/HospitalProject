from django import forms

from HospitalApp.models import Reg


class hospitalform(forms.ModelForm):
    class Meta:
        model= Reg
        fields= '__all__'