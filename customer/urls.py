"""
URL configuration for trigoblyss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from customer import views

urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('homepage', views.homepage, name='homepage'),
    path('date', views.date, name='date'),
    path('date_store/<int:id>', views.date_store, name='date_store'),
    path('register', views.register, name='register'),
    path('store', views.store, name='store'),
    path('login1', views.login1, name='login1'),
    path('checklogin', views.checklogin, name='checklogin'),
    path('contactus', views.contactus, name='contactus'),
    path('store1', views.store1, name='store1'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('feedback', views.feedback, name='feedback'),
    path('store2', views.store2, name='store2'),
    path('payment1/<int:id>', views.payment1, name='payment1'),
    path('payment1_store', views.payment1_store, name='payment1_store'),
    path('booking_data', views.booking_data, name='booking_data'),
    path('payment_process', views.payment_process, name='payment_process'),
    path('packagedetail/<int:id>', views.packagedetail, name='packagedetail'),
    path('logout', views.logout, name='logout'),
    path('packages', views.packages, name='packages'),
    path('success', views.success, name='success'),
    path('policy', views.policy, name='policy'),
    path('terms', views.terms, name='terms'),
    path('profile', views.profile, name='profile'),
    path('profile_store', views.profile_store, name='profile_store'),
    path('page_404', views.page_404, name='page_404'),
    path('page_500', views.page_500, name='page_500'),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('find', views.find, name='find'),
    path('all_plans', views.all_plans, name='all_plans'),
    path('all_places', views.all_places, name='all_places'),
    path('placedetail/<int:id>', views.placedetail, name='placedetail'),
    path('forgotpage', views.forgotpage, name='forgotpage'),
    path('forgot_password_check', views.forgot_password_check, name='forgot_password_check'),
    path('change_password', views.change_password, name='change_password'),
    path('change_password_update', views.change_password_update, name='change_password_update'),
    
]


