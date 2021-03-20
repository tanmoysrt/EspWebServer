from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentsData, AttendenceData, SchoolRegistration
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import datetime
from espwebserver.sms import sendSms


SCHOOL_REACHED = "Your son/daughter has reached school at {}"
SCHOOL_LEFT = "Your son/daughter has left school at {}"


def getStudentId(card_id):
    try:
        student = StudentsData.objects.get(issued_card_uid = card_id)
        return str(student.id)
    except:
        return "000000"


@csrf_exempt
def verifyMaskAndGiveAttendence(request):
    try:
        api_key = request.POST.get("api_key","")
        card_idd = request.POST.get("card_id","")
        school_id = SchoolRegistration.objects.get(api_key=api_key).id
        student = StudentsData.objects.get(issued_card_uid = card_idd)
        name =  student.name
        guardian_phone_no = student.guardian_phone_no
        if student.school.id == school_id:
            attendencelog = AttendenceData.objects.filter(date=datetime.datetime.now().date()).filter(student_id=student.id)
            if len(attendencelog)  == 0:
                log = AttendenceData.objects.create(
                    student = student,
                )
                log.save()
                sendSms(guardian_phone_no,SCHOOL_REACHED.format(str(datetime.datetime.now().time())))
            else :
                log = attendencelog[0]
                print("Hitted")
                log.exit_Time = datetime.datetime.now().time()
                log.status = "left"
                log.save()
                sendSms(guardian_phone_no,SCHOOL_LEFT.format(str(datetime.datetime.now().time())))

            return HttpResponse(f"{str(name[:6]).upper()} Roll - {str(student.rollno)}")
    except Exception as e:
        print(str(e))
    
    return HttpResponse(f"FAILED")