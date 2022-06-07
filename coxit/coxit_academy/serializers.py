from asyncore import read
from pkg_resources import require
from rest_framework import serializers

from .models import AcademyStudent
from coxit_staff.models import CoxitWorker

# class AcademyStudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=40, required=True)
#     last_name = serializers.CharField(max_length=40, required=True)
#     birthday = serializers.DateField(required=False)
#     phone_number = serializers.CharField(required=False, max_length=15)
#     email = serializers.CharField(max_length=40, required=True)
#     mentor = serializers.ReadOnlyField(source="coxit_worker.last_name")
    
#     def create(self, validated_data):
#         return AcademyStudent.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.birthday = validated_data.get('birthday', instance.birthday)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#         instance.email = validated_data.get('email', instance.email)
        
#         instance.save()
#         return instance
    
    
class AcademyStudentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = AcademyStudent
        fields = ['id', 'first_name', 'last_name', 'birthday', 'phone_number', 'email', 'mentor']
   
        
class CoxitWorkerSerializer(serializers.ModelSerializer):
    
    students = serializers.HyperlinkedRelatedField(many=True, view_name='student-single', read_only=True,)
    
    class Meta:
        model = CoxitWorker
        fields = ['id', 'first_name', 'last_name', 'students']