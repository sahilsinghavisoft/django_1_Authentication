from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.registerpage,name="registerpage"),
    path('register/',views.userRegistration,name='register'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('loginuser/',views.loginuser,name='loginuser')
]