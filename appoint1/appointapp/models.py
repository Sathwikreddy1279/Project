from django.db import models
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
