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
from myadmin import views

urlpatterns = [
   path('layout', views.layout, name='layout'),
   path('header', views.header, name='header'),
   path('footer', views.footer, name='footer'),
   path('sidebar', views.sidebar, name='sidebar'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('common_form', views.common_form, name='common_form'),
   path('common_table', views.common_table, name='common_table'),
   path('add_category', views.add_category, name='add_category'),
   path('store4', views.store4, name='store4'),
   path('all_category', views.all_category, name='all_category'),
   path('update/<int:id>', views.update, name='update'),
   path('edit/<int:id>', views.edit, name='edit'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('all_hotel', views.all_hotel, name='all_hotel'),
   path('hotel/<int:id>', views.hotel, name='hotel'),
   path('update1/<int:id>', views.update1, name='update1'),
   path('update_hotel/<int:id>', views.update_hotel, name='update_hotel'),
   path('edit1/<int:id>', views.edit1, name='edit1'),
   path('delete1/<int:id>', views.delete1, name='delete1'),
   path('add_hotel', views.add_hotel, name='add_hotel'),
   path('store5', views.store5, name='store5'),
   path('add_travel', views.add_travel, name='add_travel'),
   path('store6', views.store6, name='store6'),
   path('all_travel', views.all_travel, name='all_travel'),
   path('travel/<int:id>', views.travel, name='travel'),
   path('update2/<int:id>', views.update2, name='update2'),
   path('update_travel/<int:id>', views.update_travel, name='update_travel'),
   path('edit2/<int:id>', views.edit2, name='edit2'),
   path('delete2/<int:id>', views.delete2, name='delete2'),
   path('add_place', views.add_place, name='add_place'),
   path('store7', views.store7, name='store7'),
   path('all_place', views.all_place, name='all_place'),
   path('place/<int:id>', views.place, name='place'),
   path('update3/<int:id>', views.update3, name='update3'),
   path('update_place/<int:id>', views.update_place, name='update_place'),
   path('edit3/<int:id>', views.edit3, name='edit3'),
   path('delete3/<int:id>', views.delete3, name='delete3'),
   path('add_plan', views.add_plan, name='add_plan'),
   path('store8', views.store8, name='store8'),
   path('all_plan', views.all_plan, name='all_plan'),
   path('plan/<int:id>', views.plan, name='plan'),
   path('update4/<int:id>', views.update4, name='update4'),
   path('update_plan/<int:id>', views.update_plan, name='update_plan'),
   path('edit4/<int:id>', views.edit4, name='edit4'),
   path('delete4/<int:id>', views.delete4, name='delete4'),
   path('customer', views.customer, name='customer'),
   path('sub_customer', views.sub_customer, name='sub_customer'),
   path('booking', views.booking, name='booking'),
   path('add_state', views.add_state, name='add_state'),
   path('store9', views.store9, name='store9'),
   path('all_state', views.all_state, name='all_state'),
   path('update_state/<int:id>', views.update_state, name='update_state'),
   path('update5/<int:id>', views.update5, name='update5'),
   path('edit5/<int:id>', views.edit5, name='edit5'),
   path('delete5/<int:id>', views.delete5, name='delete5'),
   path('add_city', views.add_city, name='add_city'),
   path('store10', views.store10, name='store10'),
   path('all_city', views.all_city, name='all_city'),
   path('update_city/<int:id>', views.update_city, name='update_city'),
   path('update6/<int:id>', views.update6, name='update6'),
   path('edit6/<int:id>', views.edit6, name='edit6'),
   path('delete6/<int:id>', views.delete6, name='delete6'),
   path('add_area', views.add_area, name='add_area'),
   path('store11', views.store11, name='store11'),
   path('all_area', views.all_area, name='all_area'),
   path('update_area/<int:id>', views.update_area, name='update_area'),
   path('update7/<int:id>', views.update7, name='update7'),
   path('edit7/<int:id>', views.edit7, name='edit7'),
   path('delete7/<int:id>', views.delete7, name='delete7'),
   path('add_plans_places/<int:id>', views.add_plans_places, name='add_plans_places'),
   path('insert_plans_places', views.insert_plans_places, name='insert_plans_places'),
   path('add_plans_hotels/<int:id>', views.add_plans_hotels, name='add_plans_hotels'),
   path('insert_plans_hotels', views.insert_plans_hotels, name='insert_plans_hotels'),
   path('feedback', views.feedback, name='feedback'),
   path('sub_feedback/<int:id>', views.sub_feedback, name='sub_feedback'),
   path('inquiry', views.inquiry, name='inquiry'),
   path('sub_inquiry/<int:id>', views.sub_inquiry, name='sub_inquiry'),
   path('login', views.login, name='login'),
   path('profile', views.profile, name='profile'),
   path('customer_store', views.customer_store, name='customer_store')
]


