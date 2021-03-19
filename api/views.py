from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentsData, AttendenceData, SchoolRegistration
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verifyMaskAndGiveAttendence(request):
    name = ""
    try:
        api_key = request.POST.get("api_key","")
        card_idd = request.POST.get("card_id","")
        school_id = SchoolRegistration.objects.get(api_key=api_key).id
        student = StudentsData.objects.get(issued_card_uid = card_idd)
        if student.school.id == school_id:
            log = AttendenceData.objects.create(
                student = student,
            )
            name =  student.name
            log.save()
            return HttpResponse(f"{str(name[:6]).upper()} Roll - {str(student.rollno)}")
    except Exception as e:
        print(str(e))
    
    return HttpResponse(f"FAILED")