"""comapany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from company_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="home"),
    path('createaccount/',createaccount,name="createaccount"),
    path('login/',login_view,name="login"),
    path('about/',about,name="about"),
    path('aboutsociety/',aboutsociety,name="about society"),
    path('activities/',activities,name="activities"),
    path('contact/',contact,name="contact"),
    path('management/',management,name="management"),
    path('notifications/',notifications,name="notifications"),
    path('photos/',photos,name="photos"),
    path('recentactivities/',recentactivity,name="recent activities"),
    path('services/',services,name="services"),
    path('sharemembers/',sharemembers,name="sharemembers"),
    path('terms/',terms,name="terms"),
    path('testimonials/',testimonials,name="testimonials"),
    path('upcomingactivities/',upcomingactivities,name="upcoming activities"),
    path('vision/',vision,name="vision"),
    path('signout/',signout,name="signout"),
    path('logout/',logout_view,name="logout"),
    path('applicationform/',applicationform,name="applicationform"),
    path('adminlogin/',adminlogin,name="adminlogin")

]
