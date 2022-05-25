from django.urls import path

from BlogApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginview,name='login'),
    path('adminview',views.adminhome,name='adminview'),
    path('addprofile',views.profile_add,name='addprofile'),
    path('viewprofile',views.profile_view,name='viewprofile'),
]