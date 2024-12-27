from rest_framework.response import Response
from rest_framework.decorators import api_view
from demoapi.models import Employee
from .serializer import EmployeeSerializer
from rest_framework import serializers
from rest_framework import status

# Create your views here.

@api_view(http_method_names=['GET'])
def view_first_api(request):
    msg="Hello Api how are you??"
    resp=Response(data=msg)
    return resp

@api_view(['POST'])
def view_Insert_Employee(request):
    emp_serializer=EmployeeSerializer(data=request.data)
    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This Employee already Exist!!")
    if emp_serializer.is_valid():
        emp_serializer.save()
        return Response(status==status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_Show_Employee(request):
    # checking for the parameters from the URL
    if request.query_params:
        emp = Employee.objects.filter(**request.query_params.dict())
    else:
        emp = Employee.objects.all()
    # if there is something in Employee else raise error
    if emp:
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_GetById_Employee(request,eid):
    emp = Employee.objects.get(id=eid)
    if emp:
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def view_Update_Employee(request,eid):
    emp = Employee.objects.get(id=eid)
    emp_serial = EmployeeSerializer(instance=emp,data=request.data)
    if emp_serial.is_valid():
        emp_serial.save()
        return Response(status==status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def view_Delete_Employee(request,eid):
    emp = Employee.objects.get(id=eid)
    if emp:
        emp.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)