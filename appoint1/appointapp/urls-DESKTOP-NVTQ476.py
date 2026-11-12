from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',views.home,name='home'),
    path('book_appointment', views.book_appointment, name='book_appointment'),
    path('main',views.main,name='main'),
    path('team',views.team,name='team'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('address',views.address,name='address'),
    path('service',views.service,name='service'),
    path( 'index',views.index,name='index'),
    path('login',views.login,name='login'), 
    path( 'index1',views.index1,name='index1'),
    path('login1',views.login1,name='login1'), 
    path('login2',views.login2,name='login2'), 
    path('logout',views.logout,name='logout'),
    path('patient',views.patient,name='patient'), 
    path('patientappointment',views.patientappointment,name='patientappointment'), 
    path('doctor',views.doctor,name='doctor'),
    path('myappointments',views.myappointments,name='myappointments'), 
    path('forgotpassword',views.forgotpassword,name='forgotpassword'), 
    path('viewappointment', views.viewappointment, name='viewappointment'),
    path('editappointment/<int:appoint_id>/', views.editappointment, name='editappointment'),
    path('deleteappointment/<str:appoint_id>/', views.deleteappointment, name='deleteappointment'),
    path('addappointment', views.addappointment, name='addappointment'),
    path('confirm/<int:appoint_id>/', views.confirm_appointment, name='confirm_appointment'),
    path('cancel/<int:appoint_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('teaml',views.teaml,name='teaml'),
    path('patientprofile',views.patientprofile,name='patientprofile'),
    path('doctorprofile',views.doctorprofile,name='doctorprofile'),
    path('patientpage',views.patientpage,name='patientpage'),
    path('doctorpage',views.doctorpage,name='doctorpage'),
    path('patientcancel/<int:appoint_id>/', views.patientcancel, name='patientcancel'),
    path("razorpay/create-order/", views.create_razorpay_order, name="razorpay_create_order"),
    path("razorpay/verify/", views.verify_razorpay_payment, name="razorpay_verify"),
]

# +static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

