from django.shortcuts import render
from .models import contact,Hightlight,Hobbies,skills,about_you,project,Personal_info,profile
from django.core.mail import send_mail
from mypro import settings
# Create your views here.
def home(r):
    context = {}
    hlight= Hightlight.objects.all()
    hby= Hobbies.objects.all()
    skl = skills.objects.all()
    aby= about_you.objects.all()
    pro = project.objects.all()
    pinfoo = Personal_info.objects.all()
    pic= profile.objects.all()
    # for i in pic:
    #     print(i.img)
   
    context={"light" : hlight,"hoby":hby,"skil":skl,"abtyou":aby,"projects":pro,"pinfo":pinfoo,"pic":pic}
    if r.method=="POST":
        nm=r.POST['name']
        email=r.POST['email']
        sub=r.POST['subject']
        msg=r.POST['message']
        a=contact(name=nm,email=email,subject=sub,message=msg)
        a.save()
        send_mail(
        "<Portfoliogagandeep>     " + "    "+sub,
       "Name :" + nm +"\n"+ "Email :"+ email +"\n"+"Subject :"+ sub +"\n"+"Message : " + msg,
        settings.EMAIL_HOST_USER,
       [settings.EMAIL_HOST_USER,],
        fail_silently=False,
        )

    return render(r,"index.html",context)