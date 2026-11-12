from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from .models import *
import datetime
from django.core.mail import EmailMessage, message
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse

# Assuming you have an appointment ID, replace '123' with the actual appointment ID


from django.http import HttpRequest,HttpResponse
import mysql.connector


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def address(request):
    return render(request,'address.html')
def main(request):
    return render(request,'main.html')
def service(request):
    return render(request,'service.html')
def team(request):
    return render(request,'team.html')
def teaml(request):
    return render(request,'teaml.html')
def patientprofile(request):
    return render(request,'patientprofile.html')
def patientpage(request):
    return render(request,'patientpage.html')
def doctorpage(request):
    return render(request,'doctorpage.html')
def doctorprofile(request):
    return render(request,'doctorprofile.html')
def index(request):

    if(request.method=="POST"):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        fname=request.POST['fn']
        uname=request.POST['un']
        pwd=request.POST['pwd']
        gender=request.POST['gselected']
        phone=request.POST['phone']
        email=request.POST['e']
        meb=request.POST['hselected']
        address=request.POST['address']
        mycursor = conn.cursor()
        mycursor.execute("insert into patients(pname,uname,pwd,gender,phone,email,MI,address) values('"+fname+"','"+uname+"','"+pwd+"','"+gender+"', '"+phone+"','"+email+"', '"+meb+"','"+address+"')")
        conn.commit()    
        return render(request,"user.html",{"status":"you can login"})
    else:
        return render(request,'reg.html')
def login(request):
    if(request.method=="POST"):
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from patients where uname='"+uname+"' and pwd='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            pid = result[0] 
            request.session["pid"]=pid
            request.session["username"]=uname
            return redirect('patientpage')
        
        else:
            return render(request,"user.html",{"status":"invalid credentials"})
    else:
        return render(request,'user.html')  
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import mysql.connector
from .models import patients

def patient(request):
    if 'username' in request.session:
        uname = request.session['username']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM patients WHERE uname='" + uname + "'")
        result = mycursor.fetchall()
        std = []

        for x in result:
            s = patients()
            s.pid = x[0]
            s.pname = x[1]
            s.uname = x[2]
            s.pwd = x[3]
            s.gender = x[4]
            s.phone = x[5]
            s.email = x[6]
            s.MI = x[7]
            s.address = x[8]
            std.append(s)

        conn.close()

        return render(request, 'patientprofile.html', {"uname": uname, "patientlist": std})
    else:
        messages.error(request, 'You are not logged in.')
        return HttpResponse("You are not logged in.")


def patientappointment(request):
    pid=''
    if('pid' in request.session and request.session['pid']!=None):
        pid=request.session['pid'] 
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("select  appointments.appoint_id,appointments.pid,appointments.did,appointments.dname, appointments.appointment_date,appointments.appointment_time,appointments.pname  from appointments JOIN patients ON appointments.pid=patients.pid where appointments.pid='"+str(pid)+"' and   appointments.is_confirmed= 1")
        result=mycursor.fetchall()
        print(result)
        std =[]
        for x in result:
           s=myappoint()
           s.appoint_id=x[0]
           s.pid=x[1]
           s.did=x[2]
           s.dname=x[3]
           s.appointment_date=x[4]
           s.appointment_time=x[5]
           s.pname=x[6]
           std.append(s)
        conn.close()
        if result:
           return render(request,'view2.html',{"appointmentlist":std})
        else:
            return render(request,'no_appointments.html')
   
def index1(request):

    if(request.method=="POST"):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        fname=request.POST['fn']
        uname=request.POST['un']
        pwd=request.POST['pwd']
        gender=request.POST['gselected']
        speciality=request.POST['speciality']
        designation=request.POST['designation']
        phone=request.POST['phone']
        email=request.POST['e']
        address=request.POST['address']
        mycursor = conn.cursor()
        mycursor.execute("insert into doctor(dname,uname,pwd,gender, speciality,designation,phone,email,address) values('"+fname+"','"+uname+"','"+pwd+"','"+gender+"','"+speciality+"','"+designation+ "','"+phone+"','"+email+"','"+address+"')")
        conn.commit()    
        return render(request,"doctor.html",{"status":"you can login"})
    else:
        return render(request,'reg1.html')
def login1(request):
    if(request.method=="POST"):
        uname=request.POST['un']
        pwd=request.POST['pwd']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from doctor where uname='"+uname+"' and pwd='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session["username"]=uname
            return redirect('doctorpage')
        else:
            return render(request,"doctor.html",{"status":"invalid credentials"})
    else:
        return render(request,'doctor.html')       
def doctor(request):
    uname=''
    if('username' in request.session and request.session['username']!=None):
        uname=request.session['username']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from  doctor where  uname='"+uname+"'")
        result=mycursor.fetchall()
        std=[]
        for s in result:
            p=doctors()
            p.did=s[0]
            p.dname=s[1]
            p.uname=s[2]
            p.pwd=s[3]
            p.gender=s[4]
            p.speciality=s[5]
            p.designation=s[6]
            p.phone=s[7]
            p.email=s[8]
            p.address=s[9]
            std.append(p) 
        return render(request,'doctorprofile.html',{"uname":uname,"doctorlist":std})

    else:
        return redirect('login1')   
def myappointments(request):
    did=''
    if('did' in request.session and request.session['did']!=None):
        did=request.session['did']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("select  appointments.appoint_id,appointments.pid,appointments.did,appointments.dname, appointments.appointment_date,appointments.appointment_time from appointments JOIN doctor ON appointments.did=doctor.did where  appointments.did='"+str(did)+"' and appointments.is_confirmed= 1")
        result=mycursor.fetchall()
        std =[]
        for s in result:
           p=myappointment()
           p.appoint_id=s[0]
           p.pid=s[1]
           p.did=s[2]
           p.dname=s[3]
           p.appointment_date=s[4]
           p.appointment_time=s[5]
           std.append(p)
       
        return render(request,'view1.html',{ "appointmentlist":std})

    else:
        return redirect('login2')             
def login2(request):
    if(request.method=="POST"):
        uname=request.POST['un']
        pwd=request.POST['pwd']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from admin where admin='"+uname+"' and password='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session["username"]=uname
            return redirect('viewappointment')
        else:
            return render(request,"admin.html",{"status":"invalid credentials"})
    else:
        return render(request,'admin.html')    

def logout(request):
        try:
            if(request.session['username']!=None):
                 del request.session["username"]
        except KeyError:
            pass
        return redirect('home')
from django.shortcuts import render, redirect
import mysql.connector
from .models import appointments
from django.contrib import messages  # Import the messages framework

def book_appointment(request):
    if(request.method == 'POST'):
       request.session["pid"]=pid
       conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
       pid=request.POST['pid']
       did=request.POST['did']       
       speciality=request.POST['speciality']
       doctor=request.POST['doctor']
       name=request.POST['name']
       email=request.POST['email']
       date=request.POST['date']
       time=request.POST['time']
       mycursor = conn.cursor()
       mycursor.execute("INSERT INTO appointments(pid,did,speciality,dname,appointment_date, appointment_time,email,pname) values('"+pid+"','"+did+"','"+speciality+"','"+doctor+"','"+date+"','"+time+"','"+email+"','"+name+"')")
       conn.commit()    
       return redirect("patientpage")
    else:
        return render(request,'appointment.html')  

def editappointment(request,appoint_id):
    if(request.method=="POST"):
        pname=request.POST['name']
        dname=request.POST['doctor']
        date=request.POST['date']
        time=request.POST['time']
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"        
            )
        mycursor = conn.cursor()

        mycursor.execute("update appointments set dname="+dname+",appointment_date="+date+"  ,appointment_time"+time+",  pname='"+pname+"' where appoint_id="+appoint_id+ "")
        conn.commit()
        return redirect('addappointments')
    
    else:

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"        
            )
        mycursor = conn.cursor()
        mycursor.execute("select * from appointments where appoint_id="+str(appoint_id)+" ")
        result=mycursor.fetchone()
        std =[]
        for p in result:
           p=appointments()
           p.appoint_id=result[0]
           p.pid=result[1]
           p.did=result[2]
           p.speciality=result[3]
           p.dname=result[4]
           p.appointment_date=result[5]
           p.appointment_time=result[6]
           p.pname=result[7]
           p.email=result[8]
           
           std.append(p)
        return render(request,'editappointment.html',{"appointmentlist":std})
    
def deleteappointment(request,appoint_id):    
    print('in delete')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="doctorappointment"        
        )
    mycursor = conn.cursor()
    mycursor.execute("delete from appointments where appoint_id="+appoint_id+"")
    conn.commit()
    return redirect('viewappointment')
def addappointment(request):  
    if(request.method=="POST"):
        print('in post')
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        speciality=request.POST['speciality']
        doctor=request.POST['doctor']
        name=request.POST['name']
        email=request.POST['email']
        date=request.POST['date']
        time=request.POST['time']
        mycursor = conn.cursor()
        mycursor.execute("INSERT INTO appointments(speciality,dname,appointment_date, appointment_time,email,pname) values('"+speciality+"','"+doctor+"','"+date+"','"+time+"','"+email+"','"+name+"')")
        conn.commit()    
        return render(request,"view.html")
    
    else:
        return render(request,'newappointment.html')
def viewappointment(request):  
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
    )
    mycursor = conn.cursor()
    mycursor.execute("select * from appointments ")
    result=mycursor.fetchall()
    std =[]
    if(result!=None):
        for s in result:
            p=appointments()
            p.appoint_id=s[0]
            p.pid=s[1]
            p.did=s[2]
            p.speciality=s[3]
            p.dname=s[4]
            p.appointment_date=s[5]
            p.appointment_time=s[6]
            p.pname=s[7]
            p.email=s[8]
            p.is_confirmed=s[9]
            std.append(p)
        return render(request,'view.html',{"appointmentlist":std})
    else:
        return render(request,'admin.html')

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Rest of your code here


def forgotpassword(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="doctorappointment"
        )
        mycursor = conn.cursor()
        # retrieve post details
        email = request.POST['email']
        mycursor.execute("SELECT pwd FROM patients WHERE email='" + email + "'")
        result = mycursor.fetchone()
        pwd = str(result[0])
        if result is not None:
            # SMTP server configuration
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'freefirekingsunny'
            # For App Password, enable 2-step verification, then create an app password
            smtp_password = 'jcvroqrjzbqoklxz'
            # Email content
            subject = 'Password recovery'
            body = 'This is a Password recovery email sent from OM SAI- Hospital. ' \
                   'Your password as per registration is: ' + pwd
            sender_email = 'freefirekingsunny@gmail.com'
            receiver_email = email
            # Create a message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            # Connect to SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            message = "Password sent to the given email ID"
            return render(request, 'user.html', {'alert_message': message})
        else:
            message = "Please enter the correct email ID"
            return render(request, 'email.html', {'alert_message': message})
    else:
        return render(request, 'email.html')


from django.db import connections

import mysql.connector
from django.shortcuts import redirect

import mysql.connector
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings

def confirm_appointment(request, appoint_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="doctorappointment" 
        )
        mycursor = conn.cursor()
        # retrieve post details
        mycursor.execute("SELECT email FROM appointments WHERE appoint_id='" + str(appoint_id) + "'")
        result = mycursor.fetchone()
         # Send a confirmation email
        subject = 'Appointment Confirmed'
        message = 'Your appointment has been confirmed. Thank you!'
        from_email = settings.EMAIL_HOST_USER
        receiver_email = result

        send_mail(subject, message, from_email,receiver_email, fail_silently=False)
        # Create a cursor object to interact with the database
        mycursor = conn.cursor()
        sql_query = "UPDATE appointments SET is_confirmed = 1 WHERE appoint_id ='" +str(appoint_id)+"'"
        mycursor.execute(sql_query)
        conn.commit()
        conn.close()
        return redirect('viewappointment')

    except mysql.connector.Error as err:
            # Handle any database errors
        print(f"Database error: {err}")
        return redirect('patientpage')  
       
from django.http import HttpResponse, HttpResponseRedirect




def cancel_appointment(request, appoint_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="doctorappointment" 
        )
        mycursor = conn.cursor()
        # retrieve post details
        mycursor.execute("SELECT email FROM appointments WHERE appoint_id='" + str(appoint_id) + "'")
        result = mycursor.fetchone()
         # Send a confirmation email
        subject = 'Appointment Cancelled'
        message = 'Your appointment has been cancelled. Thank you!'
        from_email = settings.EMAIL_HOST_USER
        receiver_email = result

        send_mail(subject, message, from_email,receiver_email, fail_silently=False)
        # Create a cursor object to interact with the database
        mycursor = conn.cursor()
        sql_query = "UPDATE appointments SET is_confirmed = 0 WHERE appoint_id ='" +str(appoint_id)+"'"
        mycursor.execute(sql_query)
        conn.commit()
        conn.close()
        return redirect('viewappointment')

    except mysql.connector.Error as err:
            # Handle any database errors
        print(f"Database error: {err}")
        return redirect('/')  

def patientcancel(request, appoint_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="doctorappointment" 
        )
        mycursor = conn.cursor()
        # retrieve post details
        mycursor.execute("SELECT email FROM appointments WHERE appoint_id='" + str(appoint_id) + "'")
        result = mycursor.fetchone()
         # Send a confirmation email
        subject = 'Appointment Cancelled'
        message = 'Your appointment has been cancelled. Thank you!'
        from_email = settings.EMAIL_HOST_USER
        receiver_email = result

        send_mail(subject, message, from_email,receiver_email, fail_silently=False)
        # Create a cursor object to interact with the database
        mycursor = conn.cursor()
        sql_query = "UPDATE appointments SET is_confirmed = 0 WHERE appoint_id ='" +str(appoint_id)+"'"
        mycursor.execute(sql_query)
        conn.commit()
        conn.close()
        return redirect('patientappointment')

    except mysql.connector.Error as err:
            # Handle any database errors
        print(f"Database error: {err}")
        return redirect('patientpage')  
       
from django.http import HttpResponse, HttpResponseRedirect

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings

@csrf_exempt
def verify_razorpay_payment(request):
    if request.method == "POST":
        razorpay_client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )

        try:
            razorpay_client.utility.verify_payment_signature({
                'razorpay_order_id': request.POST.get('razorpay_order_id'),
                'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                'razorpay_signature': request.POST.get('razorpay_signature'),
            })

            return JsonResponse({
                "status": "success",
                "message": "Payment verified successfully"
            })

        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({
                "status": "failed",
                "message": "Payment verification failed"
            }, status=400)
            

    # 👇 VERY IMPORTANT
    return HttpResponseBadRequest("Invalid request method")
