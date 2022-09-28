from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age =  serializers.IntegerField()
    joining_date = serializers.DateTimeField('Joining date')
    salary = serializers.IntegerField()
    role = serializers.CharField(max_length=200)
    performance_persent = serializers.IntegerField(default=0)
