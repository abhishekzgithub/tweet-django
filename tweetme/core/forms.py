from django import forms
class UserForm(forms.Form):
    name=forms.CharField(max_length=20,help_text="Please enter your name")
    age=forms.IntegerField()
    email=forms.EmailField()
    phone_number=forms.IntegerField()
