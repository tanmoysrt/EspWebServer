from django.urls import path,include
from . import views


urlpatterns = [
    path('verify/',views.verifyMaskAndGiveAttendence)
]