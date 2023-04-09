from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female','FEMALE'), ('other', 'OTHER')]
    firstName=forms.CharField(validators=[
        validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    lastName=forms.CharField()
    email=forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER), required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
    file = forms.FileField(widget=forms.FileInput, required=False)
    
    '''
    def clean_firstName(self):
        inputFirstname = self.cleaned_data['firstName']
        if len(inputFirstname) > 30:
            raise forms.ValidationError('The max length of First Name is 30 characters')
        return inputFirstname
    
    def clean_lastName(self):
        inputLastname = self.cleaned_data['lastName']
        if len(inputLastname) > 30:
            raise forms.ValidationError('The max length of Last Name is 30 characters')
        return inputLastname
    
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('Invalid Email : Missing @ in email')
        return inputEmail
    
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName) > 30:
            raise forms.ValidationError('The max length of First Name is 30 characters')
        
        inputEmail = user_cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('Invalid Email : Missing @ in email')
    '''