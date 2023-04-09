from django import forms

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female','FEMALE'), ('other', 'OTHER')]
    firstName=forms.CharField()
    lastName=forms.CharField()
    email=forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER), required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
