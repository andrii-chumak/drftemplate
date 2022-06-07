from cgitb import lookup
from functools import partial
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

from .serializers import AcademyStudentSerializer, CoxitWorkerSerializer
from .models import AcademyStudent
from coxit_staff.models import CoxitWorker
from .permissions import IsMentorOrReadOnly

# @api_view(['GET', 'POST'])
# def students_list(request):
#     if request.method == "GET":
#         students = AcademyStudent.objects.all()
#         serializer = AcademyStudentSerializer(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         serializer = AcademyStudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT'])
# def student_single(request, pk):
#     student = get_object_or_404(AcademyStudent, pk=pk)
        
#     if request.method == 'GET':
#         serializer = AcademyStudentSerializer(student)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = AcademyStudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
    
class StudentList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        print('We in get method')
        students = AcademyStudent.objects.all()
        serializer = AcademyStudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AcademyStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StudentSingle(APIView):
    permission_classes = [IsMentorOrReadOnly]
    
    def get(self, request, pk):
        student = get_object_or_404(AcademyStudent, pk=pk)
        serializer = AcademyStudentSerializer(student)
        return Response(serializer.data)
    
    def post(self, request, pk):
        student = get_object_or_404(AcademyStudent, pk=pk)
        serializer = AcademyStudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class StudentList(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin
                  ):
    
    queryset = AcademyStudent.objects.all()
    serializer_class = AcademyStudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class WorkerSingle(generics.RetrieveUpdateAPIView):
    queryset=CoxitWorker.objects.all()
    serializer_class=CoxitWorkerSerializer
    