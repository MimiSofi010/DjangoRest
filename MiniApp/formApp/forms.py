from django import forms

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female','FEMALE'), ('other', 'OTHER')]
    firstName=forms.CharField()
    lastName=forms.CharField()
    email=forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
