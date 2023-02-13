from django import forms
from .models import *
class Muallifform(forms.Form):
    ism = forms.CharField(min_length=3, max_length=30)
    tirik = forms.ChoiceField(choices=[("ha","ha"), ("yoq", "yoq")])
    kitob_soni = forms.IntegerField(min_value=0, max_value=10)
    jinsi = forms.ChoiceField(choices=[("erkak","erkak"),("ayol","ayol")])
    tugulgan_sana = forms.DateField(required=False)

class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields='__all__'
class Recordform(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'
class Adminform(forms.Form):
    ism = forms.CharField(min_length=3, max_length=30)
    ish_vaqti = forms.TimeField(required=False)

