from django import forms
from modelForms.models import Project

class ProjectForms(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'