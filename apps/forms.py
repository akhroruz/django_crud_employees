from django.forms import ModelForm
from apps.models import Employee


class FormEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'year', 'address', 'phone']
