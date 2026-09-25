from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='/admin')
def view_all(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request,'view_all.html',context)  


@login_required(login_url='/admin')
def add_emp(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        new_emp = Employee(first_name=first_name, last_name=last_name,salary=salary,bonus=bonus,phone=phone , dept=dept,role=role ,location=location, hire_date= datetime.now())
        new_emp.save()
        messages.success(request, 'Employee successfully delete ho gaya hai!')
        return redirect('add_emp')

    elif request.method == 'GET':
            return render(request,'add_emp.html')

    else:
        return HttpResponse('An Error! Occurred Please Try Again')


@login_required(login_url='/admin')
def filter_emp(request):

    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name)|Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept = dept)
        if role:
            emps = emps.filter(role = role)

        context = {
            'emps' : emps
        }

        return render(request,'view_all.html',context)

    elif request.method == 'GET':
        return render(request,'filter_emp.html')

    else:
        return render(request,'filter_emp.html')
    


@login_required(login_url='/admin')
def remove_emp(request,emp_id =0):
    if emp_id:
        try:
            emp_remove = Employee.objects.get(id = emp_id)
            emp_remove.delete()
            messages.success(request, 'Employee successfully delete ho gaya hai!')
        except:
            return HttpResponse("Please enter a vaild details")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
             
    
    return render(request,'remove_emp.html',context)



