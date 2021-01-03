from django.urls import path
from myappfile import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signupuser', views.signupuser,name='signupuser'),
    path('loginuser', views.loginuser,name='loginuser'),
    path('contactus', views.contactus,name='contactus'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('logoutuser', views.logoutuser,name='logoutuser'),
]