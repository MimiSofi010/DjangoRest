from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict:dict={"name":"Milena"}
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)


def renderEmployee(request):
    myDict:dict={"id":123, "name":"John", "sal":1000}
    return render(request, 'templatesApp/employeeTemplate.html', context=myDict)
