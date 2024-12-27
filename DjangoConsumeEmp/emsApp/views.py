from django.shortcuts import render,redirect
import requests
from emsApp.models import Employee
from django.forms.models import model_to_dict
# Create your views here.

def view_show_Employee(request):
    resp=requests.get(url='http://127.0.0.1:8000/api/get/')
    if resp.status_code==200:
        data=resp.json()
    else:
        data=[]
    return render(request,'emsApp/show.html',{'data': data})


def view_add_Employee(request):
    if request.method=='GET':
        return render(request,'emsApp/addEmp.html')
    elif request.method=='POST':
        emp=Employee()
        emp.name=request.POST.get('txtName','NA')
        emp.age=request.POST.get('txtAge','NA')
        emp.mobileno=request.POST.get('txtMobile','NA')
        emp.city=request.POST.get('txtCity','NA')
        emp.salary=request.POST.get('txtSalary','NA')
        data=model_to_dict(emp)
        resp=requests.post(url='http://127.0.0.1:8000/api/insert/',json=data)
        if resp.status_code==200:
            data={'Employee Saved SuccessFully!!'}
        else:
            data={'Employee Failed!!'}
    return redirect('show')


def view_update_Employee(request,eid):
    if request.method=='GET':
        resp=requests.get(url='http://127.0.0.1:8000/api/get/{0}'.format(eid))
        if resp.status_code==200:
            data=resp.json()
        else:
            data=[]
        return render(request,'emsApp/updateEmp.html',{'data': data})
    elif request.method=='POST':
        emp=Employee()
        emp.name=request.POST.get('txtName','NA')
        emp.age=request.POST.get('txtAge','NA')
        emp.mobileno=request.POST.get('txtMobile','NA')
        emp.city=request.POST.get('txtCity','NA')
        emp.salary=request.POST.get('txtSalary','NA')
        data=model_to_dict(emp)
        resp=requests.put(url='http://127.0.0.1:8000/api/update/{0}/'.format(eid),json=data)
        if resp.status_code==200:
            data=resp.json()
        else:
            data=[]
    return redirect('show')

def view_delete_Employee(request,eid):
    resp=requests.delete(url='http://127.0.0.1:8000/api/delete/{0}'.format(eid))
    if resp.status_code==200:
        data=resp.json()
    else:
        data=[]
    return redirect('show')