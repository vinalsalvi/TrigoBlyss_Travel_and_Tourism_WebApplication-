from django.shortcuts import render , redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings 
import os
from django.http import HttpResponse
# from customer.models import Inquiry 
from myadmin.models import *
from django.contrib.auth.models import User
from customer.models import *

#common........................

def layout(request):
    context = {}
    return render(request,'myadmin/common/layout.html',context)

def header(request):
    context = {}
    return render(request,'myadmin/common/header.html',context)

def footer(request):
    context = {}
    return render(request,'myadmin/common/footer.html',context)

def sidebar(request):
    context = {}
    return render(request,'myadmin/common/sidebar.html',context)

def dashboard(request):
    context = {}
    return render(request,'myadmin/dashboard.html',context)

def common_form(request):
    context = {}
    return render(request,'myadmin/common_form.html',context)

def common_table(request):
    context = {}
    return render(request,'myadmin/common_table.html',context)

# customer

def profile(request):
    id = request.user.id
    context = {}
    return render(request,'myadmin/profile.html',context)

def customer_store(request):
    myprofile = request.FILES['profile']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myprofile.name,myprofile)
    user_id = request.user.id

    

    Customer.objects.create(profile=myprofile,user_id=user_id)
    return redirect('/myadmin/profile')



#category.............................

def add_category(request):
    context = {}
    return render(request,'myadmin/add_category.html',context)

def store4(request):
    mycategory_name = request.POST['category_name']

    Category.objects.create(category_name=mycategory_name)
    return redirect('/myadmin/all_category')

def all_category(request):
    result = Category.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_category.html',context)

def update(request,id):
    result = Category.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/update.html',context)

def edit(request,id):
    mycategory_name = request.POST['category_name']

    data = {
            'category_name' : mycategory_name
    }

    Category.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_category')


def delete(request,id):
    result = Category.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_category')

#state.........................

def add_state(request):
    context = {}
    return render(request,'myadmin/add_state.html',context)

def store9(request):
    mystate_name = request.POST['state_name']

    State.objects.create(state_name=mystate_name)
    return redirect('/myadmin/all_state')

def all_state(request):
    result = State.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_state.html',context)

def update5(request,id):
    result = State.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/update_state.html',context)

def update_state(request):
    context = {}
    return render(request,'myadmin/update_state.html',context)

def edit5(request,id):
    mystate_name = request.POST['state_name']

    data = {
            'state_name' : mystate_name
    }

    State.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_state')


def delete5(request,id):
    result = State.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_state')


#city...............................


def add_city(request):
    state = State.objects.all()
    context = {'state':state}
    return render(request,'myadmin/add_city.html',context)

def store10(request):
    mycity_name = request.POST['city_name']
    mystate_id = request.POST['state_id']

    # if request.method == "POST":
    #st = request.POST.getlist('state_id')

    # mystate_id = request.POST.getlist('state_id[]')
    # mystate_id1 = ",".join(mystate_id)

    City.objects.create(city_name=mycity_name,state_id=mystate_id) #mystate_id1
    return redirect('/myadmin/all_city')

def all_city(request):
    result = City.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_city.html',context)

def update6(request,id):
    state = State.objects.all()
    result = City.objects.get(pk=id)
    context = {'result':result,'state':state}
    return render(request,'myadmin/update_city.html',context)

def update_city(request):
    context = {}
    return render(request,'myadmin/update_city.html',context)

def edit6(request,id):
    mycity_name = request.POST['city_name']
    mystate_id = request.POST['state_id']

    data = {
            'city_name' : mycity_name,
            'state_id' : mystate_id
    }

    City.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_city')


def delete6(request,id):
    result = City.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_city')


#area...........................................


def add_area(request):
    city = City.objects.all()
    context = {'city':city}
    return render(request,'myadmin/add_area.html',context)

def store11(request):
    myarea_name = request.POST['area_name']
    mycity_id = request.POST['city_id']

    Area.objects.create(area_name=myarea_name,city_id=mycity_id)
    return redirect('/myadmin/all_area')

def all_area(request):
    result = Area.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_area.html',context)

def update7(request,id):
    city = City.objects.all()
    result = Area.objects.get(pk=id)
    context = {'result':result,'city':city}
    return render(request,'myadmin/update_area.html',context)

def update_area(request):
    context = {}
    return render(request,'myadmin/update_area.html',context)

def edit7(request,id):
    myarea_name = request.POST['area_name']
    mycity_id = request.POST['city_id']

    data = {
            'area_name' : myarea_name,
            'city_id' : mycity_id
    }

    Area.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_area')


def delete7(request,id):
    result = Area.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_area')


#hotel........................................


def add_hotel(request):
    state = State.objects.all()
    city = City.objects.all()
    area = Area.objects.all()
    context = {'state' : state , 'city' : city , 'area' : area}
    return render(request,'myadmin/add_hotel.html',context)

def store5(request):
    myhotel_name = request.POST['hotel_name']
    myemail = request.POST['email']
    mycontact = request.POST['contact']
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)
    myaddress = request.POST['address']
    mystate_id = request.POST['state_id']
    mycity_id = request.POST['city_id']
    myarea_id = request.POST['area_id']
    mydescription = request.POST['description']

    Hotel.objects.create(hotel_name=myhotel_name,email=myemail,contact=mycontact,address=myaddress,description=mydescription,image=myimage,state_id=mystate_id,city_id=mycity_id,area_id=myarea_id)
    return redirect('/myadmin/all_hotel')


def hotel(request,id):
    result = Hotel.objects.get(pk=id) 
    context = {'result':result}
    return render(request,'myadmin/hotel.html',context)

def update_hotel(request):
    context = {}
    return render(request,'myadmin/update_hotel.html',context)

def update1(request,id):
    state = State.objects.all()
    city = City.objects.all()
    area = Area.objects.all()
    result = Hotel.objects.get(pk=id)
    context = {'result':result , 'state' : state , 'city' : city , 'area' : area}
    return render(request,'myadmin/update_hotel.html',context)

def edit1(request,id):
    myhotel_name = request.POST['hotel_name']
    myemail = request.POST['email']
    mycontact = request.POST['contact']
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)
    myaddress = request.POST['address']
    mystate_id = request.POST['state_id']
    mycity_id = request.POST['city_id']
    myarea_id = request.POST['area_id']
    mydescription = request.POST['description']

    data = {
            'hotel_name' : myhotel_name,
            'email' : myemail,
            'contact' : mycontact,
            'image' : myimage,
            'address' : myaddress,
            'state_id' : mystate_id,
            'city_id' : mycity_id,
            'area_id' : myarea_id,
            'description' : mydescription
    }

    Hotel.objects.update_or_create(pk=id,defaults={'image':myimage.name})
    return redirect('/myadmin/all_hotel')

def delete1(request,id):
    result = Hotel.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_hotel')


def all_hotel(request):
    result = Hotel.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_hotel.html',context)


#travel........................................


def add_travel(request):
    context = {}
    return render(request,'myadmin/add_travel.html',context)

def store6(request):
    mytravel_name = request.POST['travel_name']
    mycontact = request.POST['contact']
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)
    myluggage = request.POST['luggage']
    myno_of_seats = request.POST['no_of_seats']
    mypickup = request.POST['pickup']
    mydrop = request.POST['drop']
    mydescription = request.POST['description']

    Travel.objects.create(travel_name=mytravel_name,drop=mydrop,description=mydescription,pickup=mypickup,luggage=myluggage,contact=mycontact,image=myimage,no_of_seats=myno_of_seats)
    return redirect('/myadmin/all_travel')

def all_travel(request):
    result = Travel.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_travel.html',context)

def travel(request,id):
    result = Travel.objects.get(pk=id) 
    context = {'result':result}
    return render(request,'myadmin/travel.html',context)

def update_travel(request):
    context = {}
    return render(request,'myadmin/update_travel.html',context)

def update2(request,id):
    result = Travel.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/update_travel.html',context)

def edit2(request,id):
    mytravel_name = request.POST['travel_name']
    mycontact = request.POST['contact']
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)
    myluggage = request.POST['luggage']
    myno_of_seats = request.POST['no_of_seats']
    mypickup = request.POST['pickup']
    mydrop = request.POST['drop']
    mydescription = request.POST['description']


    data = {
            'travel_name' : mytravel_name,
            'contact' : mycontact,
            'image' : myimage,
            'luggage' : myluggage,
            'no_of_seats' : myno_of_seats,
            'pickup' : mypickup,
            'drop' : mydrop,
            'description' : mydescription
    }

    Travel.objects.update_or_create(pk=id,defaults={'image':myimage.name})
    return redirect('/myadmin/all_travel')

def delete2(request,id):
    result = Travel.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_travel')


#place....................................



def add_place(request):
    state = State.objects.all()
    city = City.objects.all()
    area = Area.objects.all()
    context = {'state' : state , 'city' : city , 'area' : area}
    return render(request,'myadmin/add_place.html',context)

def store7(request):
    myplace_name = request.POST['place_name']
    myImage = request.FILES['Image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myImage.name,myImage)
    myaddress = request.POST['address']
    mystate_id = request.POST['state_id']
    mycity_id = request.POST['city_id']
    myarea_id = request.POST['area_id']
    mydescription = request.POST['description']

    Place.objects.create(place_name=myplace_name,Image=myImage,address=myaddress,state_id=mystate_id,city_id=mycity_id,area_id=myarea_id,description=mydescription)
    return redirect('/myadmin/all_place')

def all_place(request):
    result = Place.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_place.html',context)

def place(request,id):
    result = Place.objects.get(pk=id) 
    context = {'result':result}
    return render(request,'myadmin/place.html',context)

def update_place(request):
    context = {}
    return render(request,'myadmin/update_place.html',context)

def update3(request,id):
    state = State.objects.all()
    city = City.objects.all()
    area = Area.objects.all()
    result = Place.objects.get(pk=id)
    context = {'result':result , 'state' : state , 'city' : city , 'area' : area}
    return render(request,'myadmin/update_place.html',context)

def edit3(request,id):
    myplace_name = request.POST['place_name']
    myImage = request.FILES['Image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myImage.name,myImage)
    myaddress = request.POST['address']
    mystate_id = request.POST['state_id']
    mycity_id = request.POST['city_id']
    myarea_id = request.POST['area_id']
    mydescription = request.POST['description']

    data = {
            'place_name' : myplace_name,
            'Image' : myImage,
            'address' : myaddress,
            'state_id' : mystate_id,
            'city_id' : mycity_id,
            'area_id' : myarea_id,
            'description' : mydescription
    }

    Place.objects.update_or_create(pk=id,defaults={'Image':myImage.name})
    return redirect('/myadmin/all_place')


def delete3(request,id):
    result = Place.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_place')


#plan&places....................................


def add_plans_places(request,id):
    plan = Plan.objects.get(pk=id)
    plan_places = Place.objects.all()
    context = {'plan_places':plan_places,'plan':plan}
    return render(request,'myadmin/add_plans_places.html',context)

def insert_plans_places(request):
    myplan_name = request.POST['plan_name']
    myplace = request.POST['place_name']
    
    Plan_Place.objects.create(place_id=myplace,plan_id=myplan_name)
    return(redirect('/myadmin/all_plan'))


#plan&hotels....................................


def add_plans_hotels(request,id):
    plan = Plan.objects.get(pk=id)
    plan_hotels = Hotel.objects.all()
    context = {'plan_hotels':plan_hotels,'plan':plan}
    return render(request,'myadmin/add_plans_hotels.html',context)

def insert_plans_hotels(request):
    myplan_name = request.POST['plan_name']
    myhotel = request.POST['hotel']
    
    plan_Hotel.objects.create(hotel_id=myhotel,plan_id=myplan_name)
    return(redirect('/myadmin/all_plan'))


#plan.......................................



def add_plan(request):
    category = Category.objects.all()
    hotel = Hotel.objects.all()
    travel = Travel.objects.all()
    context = {'category' : category , 'hotel' : hotel , 'travel' : travel}
    return render(request,'myadmin/add_plan.html',context)

def store8(request):
    myplan_name = request.POST['plan_name']
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)
    myprice = request.POST['price']
    mycategory_id = request.POST['category_id']
    myhotel_id = request.POST['hotel_id']
    mytravel_id = request.POST['travel_id']
    myddate = request.POST['ddate']
    mytdate = request.POST['tdate']
    mydescription = request.POST['description']

    Plan.objects.create(plan_name=myplan_name,image=myimage,price=myprice,ddate=myddate,tdate=mytdate,category_id=mycategory_id,hotel_id=myhotel_id,travel_id=mytravel_id,description=mydescription)
    return redirect('/myadmin/all_plan')

def all_plan(request):
    result = Plan.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_plan.html',context)

def plan(request,id):
    result = Plan.objects.get(pk=id) 
    context = {'result':result}
    return render(request,'myadmin/plan.html',context)

def delete4(request,id):
    result = Plan.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_plan')

def update_plan(request):
    context = {}
    return render(request,'myadmin/update_plan.html',context)

def update4(request,id):
    category = Category.objects.all()
    hotel = Hotel.objects.all()
    travel = Travel.objects.all()
    result = Plan.objects.get(pk=id)
    context = {'result':result , 'category' : category , 'hotel' : hotel , 'travel' : travel}
    return render(request,'myadmin/update_plan.html',context)

def edit4(request,id):
    myplan_name = request.POST['plan_name']
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)
    myprice = request.POST['price']
    mycategory_id = request.POST['category_id']
    myhotel_id = request.POST['hotel_id']
    mytravel_id = request.POST['travel_id']
    myddate = request.POST['ddate']
    mytdate = request.POST['tdate']
    mydescription = request.POST['description']

    data = {
            'plan_name' : myplan_name,
            'image' : myimage,
            'price' : myprice,
            'category_id' : mycategory_id,
            'hotel_id' : myhotel_id,
            'travel_id' : mytravel_id,
            'ddate' : myddate,
            'tdate' : mytdate,
            'description' : mydescription
    }

    Plan.objects.update_or_create(pk=id,defaults={'image':myimage.name})
    return redirect('/myadmin/all_plan')

#customer / login / register 

def customer(request):
    result = User.objects.all()
    context = {'result':result}
    return render(request,'myadmin/customer.html',context)

def sub_customer(request):
    context = {}
    return render(request,'myadmin/sub_customer.html',context)

def booking(request):
    result = Booking.objects.all()
    # plan = Plan.objects.get(pk=id)
    context = {'result':result , 'plan' : plan }
    return render(request,'myadmin/booking.html',context)

def payment(request):
    context = {}
    return render(request,'myadmin/payment.html',context)

def feedback(request):
    result = Feedback.objects.all()
    context = {'result':result}
    return render(request,'myadmin/feedback.html',context)

def sub_feedback(request,id):
    result = Feedback.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/sub_feedback.html',context)

def inquiry(request):
    result = Inquiry.objects.all()
    context = {'result':result}
    return render(request,'myadmin/inquiry.html',context)

def sub_inquiry(request,id):
    result = Inquiry.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/sub_inquiry.html',context)

def login(request):
    context = {}
    return render(request,'myadmin/login.html',context)



