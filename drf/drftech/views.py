from distutils.log import ERROR
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def employee_details(request, pk):
    Emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(Emp)
   
    json_data = JSONRenderer().render(serializer.data)
    # return JsonResponse(serializer.data, safe = False)
    return HttpResponse(json_data, content_type = 'application/json')

def employee_list(request):
    Emp = Employee.objects.all()
    serializer = EmployeeSerializer(Emp, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

