from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Category(models.Model):
	category_name = models.CharField(max_length=200)

	class Meta:
		db_table = 'category'

	def __str__(self):
		return self.category_name


class Subcategory(models.Model):
	category_name = models.CharField(max_length=200)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)


class State(models.Model):
	state_name = models.CharField(max_length=200)

	class Meta:
		db_table = 'state'

	def __str__(self):
		return self.state_name


class City(models.Model):
	city_name = models.CharField(max_length=200)
	state = models.ForeignKey(State,on_delete=models.CASCADE)

	class Meta:
		db_table = 'city'

	def __str__(self):
		return self.city_name
		

class Area(models.Model):
	area_name = models.CharField(max_length=200)
	city = models.ForeignKey(City,on_delete=models.CASCADE)

	class Meta:
		db_table = 'area'

	def __str__(self):
		return self.area_name


class Hotel(models.Model):
	hotel_name = models.CharField(max_length=150)
	email = models.EmailField()
	contact = models.BigIntegerField()
	image = models.CharField(max_length=100)
	address = models.CharField(max_length=40 , default='')
	state = models.ForeignKey(State,on_delete=models.CASCADE)
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	area = models.ForeignKey(Area,on_delete=models.CASCADE)
	register_date = models.DateField(default=date.today)
	description = models.TextField()

	class Meta:
		db_table = 'hotel'

	def __str__(self):
		return self.hotel_name


class Travel(models.Model):
	travel_name = models.CharField(max_length=150) # bus , car 
	contact = models.BigIntegerField() # traveler 
	image = models.CharField(max_length=500)
	no_of_seats = models.CharField(max_length=100) # passenger
	luggage = models.CharField(max_length=100) 
	pickup = models.CharField(max_length=100)
	drop = models.CharField(max_length=100)
	description = models.TextField()

	class Meta:
		db_table = 'travel'

	def __str__(self):
		return self.travel_name


class Place(models.Model):
	place_name = models.CharField(max_length=50)
	Image = models.CharField(max_length=500)
	address = models.CharField(max_length=100)
	state = models.ForeignKey(State,on_delete=models.CASCADE) 
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	area = models.ForeignKey(Area,on_delete=models.CASCADE)
	description = models.CharField(max_length=1000)
	
	
	class Meta:
		db_table = 'place'

	def __str__(self):
		return self.place_name

# # Package table 

class Plan(models.Model):
	plan_name = models.CharField(max_length=100)
	image = models.CharField(max_length=500)
	price = models.BigIntegerField()
	ddate = models.DateField()
	tdate = models.DateField()
	category = models.ForeignKey(Category,on_delete=models.CASCADE)	
	hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
	travel = models.ForeignKey(Travel,on_delete=models.CASCADE)
	description = models.TextField()
	
	class Meta:
		db_table = 'plan'

	def __str__(self):
		return self.plan_name


class Places(models.Model):
    places_name = models.CharField(max_length=30)
	

    class Meta:
        db_table = 'places'


class Plan_Place(models.Model):
	plan = models.ForeignKey(Plan,on_delete=models.CASCADE,default='')
	place = models.ForeignKey(Place,on_delete=models.CASCADE,default='')

	class Meta():
		db_table='plan_place'

class Hotels(models.Model):
    image = models.CharField(max_length=30)
	

    class Meta:
        db_table = 'hotels'


class Plan_Hotel(models.Model):
	plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
	hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)

	class Meta():
		db_table='plan_hotel'


class Customer(models.Model):
	user = models.ForeignKey(User,blank = True , on_delete=models.CASCADE,default='')
	username = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	image = models.CharField(max_length=100)
	reg_date = models.DateField(default=date.today)
	profile = models.ImageField(upload_to = 'media' , default="login.png" , null=True , blank = True )

	class Meta:
		db_table = 'customer'

	def __str__(self):
		return self.name



