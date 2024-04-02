from django.shortcuts import render, redirect
from .forms import EmployeeForms
from .models import Employee

# Create your views here.
def employee_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForms()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForms(instance=employee)
        return render(request, "employee_register/employee_form.html", context={'form':form})

    else:
        if id==0:
            form = EmployeeForms(request.POST)

        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForms(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context=context)


def employee_delete(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=id)
        employee.delete()

    return redirect('/employee/list')
