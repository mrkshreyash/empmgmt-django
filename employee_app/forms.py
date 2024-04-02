from django import forms
from .models import Employee

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ('fullname', 'emp_id', 'mobile', 'position')

        labels = {
            "fullname":"Full Name",
            "emp_id":"Emp ID"
        }


    def __init__(self, *args, **kwargs):
        super(EmployeeForms, self).__init__(*args, **kwargs)

        self.fields['position'].empty_label = 'Select'
    