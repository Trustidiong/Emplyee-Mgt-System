from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
# RENDER THE ENTIRE LIST TO THE employee_list.html
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employeeRegister/employee_list.html', context)

def employee_form(request, id=0):

    #IMPLEMENTING A GET REQUEST
    if request.method == "GET":

        # FOR ADDING A NEW EMPLOYEE
        if id == 0:
            form = EmployeeForm()

         # FOR UPDATING AN EMPLOYEE WITH A PARTICULAR EMPLYEE ID
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employeeRegister/employee_form.html', {'form':form})
    
    #IMPLEMENTING A POST REQUEST
    else:
        # FOR INSERT OPERATION
        if id == 0:
            form = EmployeeForm(request.POST)

        # FOR UPDATE OPERATION
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)

        # COMMON TO BOTH INSERT AND UPDATE OPERATION
        if form.is_valid():
            form.save()
        #REDIRECT AFTER SAVING
        return redirect ('/employee/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect ('/employee/list')
