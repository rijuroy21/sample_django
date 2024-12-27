from django import forms

class user_form(forms.Form):
    roll=forms.IntegerField()
    name=forms.CharField()
    mark=forms.IntegerField()