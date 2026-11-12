from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class appointments:
    appoint_id:int
    pid:int
    did:int
    speciality:str
    dname:str
    appointment_date:int
    appointment_time:int
    pname:str
    email:str
    is_confirmed:bool

class patients:
     pid:int
     pname:str
     uname:str
     pwd:str
     gender:str
     phone:int
     email:str
     MI:str
     address:str

class doctors:
     did:int
     dname:str
     uname:str
     pwd:str
     gender:str
     speciality:str
     designation:str
     phone:int
     email:str
     address:str 
class myappointment:
     appoint_id:int
     pid:int
     did:int
     dname:str
     appointment_date:int
     appointment_time:int
class myappoint:
     appoint_id:int
     pid:int
     did:int
     dname:str
     appointment_date:int
     appointment_time:int
     pname:str
# models.py
class RazorpayPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()  # in paise
    status = models.CharField(max_length=20, default="CREATED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.order_id}"
     
