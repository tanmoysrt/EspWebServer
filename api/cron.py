from espwebserver.sms import sendSms
from api.models import StudentsData,AttendenceData
from django.utils import timezone
import datetime


NOT_CAME = "{} has not reached school yet"
MAY_ESCAPE = "{} may has escaped from school.Please Report"

def check_come():
    students = StudentsData.objects.all()
    attendence = AttendenceData.objects.filter(date=timezone.now().date())
    for i in students:
        try:
            data = attendence.get(student_id=i.id)
        except:
            # Logs.objects.create(student=i.student,message= NOT_CAME.format(i.student.name))
            sendSms(i.guardian_phone_no,NOT_CAME.format(i.name))


def may_escape():
    attendence = AttendenceData.objects.filter(date=datetime.datetime.now().date())
    for i in attendence:
        if i.status == "inschool":
            i.school_left_unofficially = True
            i.save()

            sendSms(i.student.guardian_phone_no,MAY_ESCAPE.format(i.student.name))