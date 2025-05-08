from django.shortcuts import render , redirect
from customer.models import *
from django.contrib import messages
from django.contrib import auth
from myadmin.models import *
from django.contrib.auth.models import User
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import LoginView


# common ....................................................................................................


def layout(request):
    context={}
    return render(request,'customer/common/layout.html',context)


def header(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan}
    return render(request,'customer/common/header.html',context)


def footer(request):
    context={}
    return render(request,'customer/common/footer.html',context)



#homepage...............................................................................................



def homepage(request):
    getplan = Plan.objects.all()
    getplace = Place.objects.all()

    context={'plans' : getplan , 'places' : getplace } 
    return render(request,'customer/homepage.html',context)



#sign up ........................................................................................................



def register(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan}
    return render(request,'customer/register.html',context)

def store(request):
    myusername = request.POST['username']
    myemail = request.POST['email']
    mypassword = request.POST['password']
    mycpassword = request.POST['cpassword']

    if mypassword == mycpassword:
        result = User.objects.create_user(username=myusername,email=myemail,password=mypassword)
        Profile.objects.create(password=mypassword,user_id=result.id)
        messages.success(request,'Sign up Successfully.')
        return redirect('/customer/login1')
    else:
        messages.error(request,'Invalid password! ')
        return redirect('/customer/register')



# login ........................................................................................................



def login1(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan}
    return render(request,'customer/login1.html',context)

def checklogin(request):
    # username = request.user.username
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(username=username, password=password )

    send_mail(
        'Login Notification',
        'You have successfully logged in.',
        'salvivinal982@gmail.com',
        [result.email],
        fail_silently=False,
    )


    if result is None:
        messages.error(request,'Invalid Username Or Password....Please Try Again! ')
        return redirect('/customer/login1')
    else:
        auth.login(request, result)
        messages.success(request,'Login Successfully.')
        return redirect('/customer/homepage')


# logout  ......................................................................................................


def logout(request):
    auth.logout(request)
    return redirect('/customer/homepage')




# package details ..........................................................................................


def packagedetail(request,id):
    plan = Plan.objects.get(pk=id)
    place = Plan_Place.objects.filter(plan_id=id) # loop
    print(place)
    hotel = Hotel.objects.get(pk=plan.hotel_id)  # no loop
    travel = Travel.objects.get(pk=plan.travel_id) # no loop
    getplan = Plan.objects.all()
     
    
    # hotel = Hotel.objects.all()
    # travel = Travel.objects.all()
    context={ 'place' : place , 'hotel' : hotel , 'travel' : travel , 'plan' : plan , 'plans' : getplan }
    return render(request,'customer/pakagedetail.html',context)



# packages & place details .....................................................................................


def packages(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan } 
    return render(request,'customer/packages.html',context)

def placedetail(request,id):
    place = Place.objects.get(pk=id)
    getplan = Plan.objects.all()
    context={ 'place' : place , 'plans' : getplan } 
    return render(request,'customer/placedetail.html',context)



# contact ...........................................................................................................


        
def contactus(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan}
    return render(request,'customer/contactus.html',context)


def store1(request):

    myname = request.POST['name']
    myemail = request.POST['email']
    mycontact = request.POST['contact']
    mymessage = request.POST['message']

    Inquiry.objects.create(name=myname,email=myemail,contact=mycontact,message=mymessage)
    return redirect('/customer/contactus')


# about ............................................................................................................


def about(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan } 
    return render(request,'customer/about.html',context)



# service ........................................................................................................


def service(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan } 
    return render(request,'customer/service.html',context)


# feedback .....................................................................................................


def feedback(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan } 
    return render(request,'customer/feedback.html',context)


def store2(request):
    user_id = request.user.id
    myrating = request.POST['rating']
    mycomment = request.POST['comment']

    Feedback.objects.create(rating=myrating,comment=mycomment,user_id=user_id)
    return redirect('/customer/feedback')




# policy & term .............................................................................................



def policy(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan } 
    return render(request,'customer/policy.html',context)


def terms(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan } 
    return render(request,'customer/terms.html',context)






# payment ....................................................................................................




def payment1(request,id):
    plan = Plan.objects.get(pk=id)
    getplan = Plan.objects.all()
    context={'plan' : plan , 'plans' : getplan }
    return render(request,'customer/payment1.html',context)


def payment_process(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan }
    return render(request,'customer/payment_process.html',context)

def payment1_store(request):
    myadult = int(request.POST['adult'])
    mychild = int(request.POST['child'])
    id      = request.POST['plan_id']

    plan = Plan.objects.get(pk=id)
    price = int(plan.price)
    half_price = float(price/2)
    total = myadult * price + mychild * half_price
    user_id = request.user.id
    getplan = Plan.objects.all()
     

    booking = Booking.objects.create(user_id=user_id,amount=total,plan_id=plan.id,adult=myadult,child=mychild)
    
    # payment
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = float(booking.amount)*100

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }
    result = User.objects.get(pk=user_id)
    payment = client.order.create(data=data)
    context = {'plan':plan, 'booking':booking,'payment' : payment,'result':result , 'plans' : getplan}
    
    return render(request,'customer/payment_process.html',context)


@csrf_exempt
def success(request):
    context = {}
    return render(request,'customer/success.html',context)



# booking detail ...............................................................................................

def booking_data(request):
    id = request.user.id
    booking = Booking.objects.filter(user_id=id)
    getplan = Plan.objects.all() 
    context={'booking':booking , 'plans' : getplan}
    return render(request,'customer/booking_data.html',context)


def cancel(request,id):
    data = Booking.objects.get(pk=id)
    data.delete()
    return redirect('/customer/booking_data')




# search ...............................................................................................



def find(request):
    search = request.POST.get('search')
    

    if search:
        # Perform the search using the search parameter
        results = Plan.objects.filter(id=search)
        
    else:
        results = None

    return render(request, 'customer/pakagedetail.html', {'results': results })

    




#forgot password.............................................................................................


def forgotpage(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan }
    return render(request,'customer/forgotpassword.html',context)


def forgot_password_check(request):
    if request.method == 'POST':
        myemail = request.POST['email']
        try:
            user = User.objects.get(email=myemail)

        except User.DoesNotExist:
            user = None
            #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char


            ##############################################################


            msg = "Hello , here it is your new password :  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'TrigoBlyss - (Your New Password)',
                msg,
                'salvivinal982@gmail.com',
                [myemail],
                fail_silently=False,
            )

            #now update the password in model
            # cuser = User.objects.get(email=myemail)
            # cuser.password = password
            user.set_password(password)
            user.save()

            print('Mail sent')
            messages.info(request, 'Password has been sent to your Gmail')
            return redirect("/customer/homepage")

        else:
            messages.info(request, 'This account does not exist')
            return redirect("/customer/forgotpage")





# change password ...........................................................................................



def change_password(request):
    getplan = Plan.objects.all()
    context={'plans' : getplan }
    return render(request,'customer/change_password.html',context)


def change_password_update(request):
    username = request.user.username
    # email = request.user.email
    old_password  = request.POST['old_password']
    new_password  = request.POST['new_password']
    rnew_password = request.POST['rnew_password']

    if new_password == rnew_password:
        user = auth.authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()

            msg = "Hello , , here it is your new password : "+new_password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'TrigoBlyss - (Your Changed New Password)',
                msg,
                'salvivinal982@gmail.com',
                [user.email],
                fail_silently=False,
            )

            profile = Profile.objects.get(user_id=request.user.id)
            Profile.objects.update_or_create(pk=profile.id,defaults={'password':new_password})
            messages.success(request, 'Password Updated Successfully.')
            return redirect('/customer/login1')
        else:
            messages.error(request, 'Invalid Password Try Again?')
            return redirect('/customer/change_password')     
    else:
         messages.error(request, 'Miss Match Password !')
         return redirect('/customer/change_password')
    


# profile ................................................................................................



def profile(request):
    id = request.user.id
    result = Customer.objects.all()   
    getplan = Plan.objects.all()
    context = {'profile':result , 'plans' : getplan}
    return render(request,'customer/profile.html',context)

def profile_store(request):
    id = request.user.id
    customer = Customer.objects.get(pk=id)
    context={customer : 'customer'}
    myimage = request.FILES['image']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)

    Profile.objects.create(image=myimage)
    return redirect('/customer/profile')

# @login_required
# def upload_profile_picture(request):
#     if request.method == 'POST':
#         # Assuming your UserProfile model has a ForeignKey relationship with the User model
#         user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#         user_profile.profile_picture = request.FILES.get('profile_picture')
#         user_profile.save()
#         return redirect('profile')  # Redirect to the user's profile page
#     return render(request, 'upload_profile_picture.html')




# date ....................................................................................................



def date(request):
    # plan = Plan.objects.get(pk=id)
    getplan = Plan.objects.all()
    context={'plans' : getplan}
    return render(request,'customer/date.html',context)

# def date_store(request):
#     myddate = request.POST['ddate']
#     mytdate = request.POST['tdate']
#     id      = request.POST['plan_id']

#     plan = Plan.objects.get(pk=id)
#     price = int(plan.price)
    

#     date = Date.objects.create(ddate=myddate,tdate=mytdate,plan_id=plan.id)
#     return redirect('/customer/pakagedetail')

def date_store(request,id):
    if request.method == 'POST':
        ddate = request.POST.get('ddate')
        tdate = request.POST.get('tdate')
        # Update package date
        plan = Plan.objects.get(pk=id)
        plan.ddate = ddate
        plan.tdate = tdate
        plan.save()
        # Store modified date in ModifiedDate table
        Date.objects.update_or_create(plan_id=id, defaults={'ddate': ddate , 'tdate' : tdate})
        return redirect('packagedetail', pk=id)
    else:
        try:
            plan = Plan.objects.get(pk=id)
        except Plan.DoesNotExist:
            # Handle case when package is not found
            return redirect('/customer/page_404')  # Redirect to an error view
        return render(request, 'date.html', {'plan_id': id, 'plan': plan})



# error .......................................................................................................


def page_404(request):
    return render(request,'customer/page_404.html')


def page_500(request):
    return render(request,'customer/page_500.html')


# all plans ..................................................................................................


def all_plans(request):
    getplan = Plan.objects.all()
    context={ 'plans' : getplan}
    return render(request,'customer/all_plans.html',context)



# all places ..................................................................................................



def all_places(request):
    getplan = Plan.objects.all()
    getplace = Place.objects.all()
    context={ 'plans' : getplan , 'places' : getplace}
    return render(request,'customer/all_places.html',context)

