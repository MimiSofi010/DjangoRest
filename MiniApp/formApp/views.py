from django.shortcuts import render
from formApp.forms import UserRegistrationForm

# Create your views here.
def userRegistrationView(request):
    form=UserRegistrationForm
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("First Name", form.cleaned_data['firstName'])
            print("Last Name", form.cleaned_data['lastName'])
            print("Email", form.cleaned_data['email'])
    return render(request, 'formApp/form.html', {'form':form})
