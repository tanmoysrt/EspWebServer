from django.db import models
from django.contrib import admin
import uuid
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class SchoolRegistration(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    username = None
    first_name=None
    last_name=None
    name = models.TextField(null=True)
    email = models.TextField(null=True,unique=True)
    api_key = models.UUIDField(default=uuid.uuid1,unique=True,editable=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    created_At = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()

    def __str__(self):
        return str(self.name)



class StudentsData(models.Model):
    school = models.ForeignKey(SchoolRegistration,on_delete=models.CASCADE)
    name = models.TextField(null=True)
    rollno = models.IntegerField(default=0,null=True)
    classno = models.CharField(max_length=15)
    issued_card_uid = models.TextField(null=True)
    guardian_phone_no = models.TextField(null=True)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.name)

class AttendenceData(models.Model):
    student = models.ForeignKey(StudentsData,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    entry_time = models.TimeField(auto_now_add=True)
    exit_Time = models.TimeField(null=True,default=None)
    school_left_unofficially = models.BooleanField(null=True,default=False)
    status = models.CharField(max_length=20,choices=(("inschool","Currently In School"),("left","Left The School")),default="inschool")

class Logs(models.Model):
    student = models.ForeignKey(StudentsData,on_delete=models.CASCADE)
    message = models.TextField(null=True,default="")
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student.name)


@admin.register(SchoolRegistration)
class SchoolRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name","email","api_key","created_At","total_no_of_student")
    fields = ("name","email","api_key")

    def total_no_of_student(self,obj):
        return len(StudentsData.objects.filter(school_id=obj.id))

@admin.register(StudentsData)
class StudentsDataAdmin(admin.ModelAdmin):
    list_display = ("name","rollno","classno","issued_card_uid","guardian_phone_no","school","total_attendence")
    fields = ("school","name","rollno","classno","issued_card_uid","guardian_phone_no")

    def total_attendence(self,obj):
        return len(AttendenceData.objects.filter(student_id=obj.id))

@admin.register(AttendenceData)
class AttendenceDataAdmin(admin.ModelAdmin):
    list_display = ("student","school_name","class_name","roll_no","date","entry_time","exit_Time","school_left_unofficially","status","mobile_number")
    fields = ("student","exit_Time","school_left_unofficially","status")
    list_filter = ("school_left_unofficially",)
    def school_name(self,obj):
        return str(obj.student.school.name)

    def class_name(Self,obj):
        return str(obj.student.classno)

    def roll_no(Self,obj):
        return str(obj.student.rollno)

    def mobile_number(self,obj):
        return str(obj.student.guardian_phone_no)

@admin.register(Logs)
class LogsData(admin.ModelAdmin):
    list_display=("student","message","created_At","mobile_number")

    def mobile_number(self,obj):
        return str(obj.student.guardian_phone_no)