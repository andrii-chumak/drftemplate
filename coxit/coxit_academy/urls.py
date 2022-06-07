from django.urls import path
from .views import StudentList, StudentSingle, WorkerSingle


urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentSingle.as_view(), name='student-single'),
    path('workers/<int:pk>/', WorkerSingle.as_view(), name='worker-single'),
]
