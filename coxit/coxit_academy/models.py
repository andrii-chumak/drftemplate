from pyexpat import model
from django.db import models
from coxit_staff.models import CoxitWorker

class AcademyStudent(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=40)
    mentor = models.ForeignKey(CoxitWorker, related_name="students", on_delete=models.SET_NULL, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "academy_students"
        

class AcademyLecture(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField(null=True)
    lecturer = models.ForeignKey(CoxitWorker, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "academy_lectures"


class AcademyAssignment(models.Model):
    link = models.CharField(max_length=50)
    deadline_date = models.DateField(null=True)    
    lecture = models.ForeignKey(AcademyLecture, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "academy_assignments"


class AssignmentSubmission(models.Model):
    link = models.CharField(max_length=50)
    student = models.ForeignKey(AcademyStudent, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AcademyAssignment, on_delete=models.CASCADE)
    revisor = models.ForeignKey(CoxitWorker, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "academy_assignment_submissions"