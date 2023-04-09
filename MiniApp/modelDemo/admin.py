from django.contrib import admin
from modelDemo.models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    fields = ('firstName', 'lastName', 'salary', 'email')
    list_display = ('id', 'firstName', 'lastName', 'salary', 'email')
    list_filter = ('lastName',)

admin.site.register(Employee, EmployeeAdmin)