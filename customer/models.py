from django.db import models
from datetime import date
from myadmin.models import Plan
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	password = models.CharField(max_length=30)
	image = models.CharField(max_length=100)


	class Meta:
		db_table = 'profile'

	def __str__(self):
		return self.user.username

class Inquiry(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	contact = models.BigIntegerField()
	message = models.CharField(max_length=200)
	date = models.DateField(default=date.today)

	class Meta:

		db_table = 'inquiry'

class Login(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	reg_date = models.DateField(default=date.today)

	class Meta:
		db_table = 'login'

	def __str__(self):
		return self.email


class Feedback(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	rating = models.BigIntegerField()
	comment = models.TextField()
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'feedback'


class Booking(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
	plan = models.ForeignKey(Plan,on_delete=models.CASCADE,default='')
	amount = models.DecimalField(max_digits=7,decimal_places=2)
	payment_mode = models.CharField(max_length=40,default="online")
	booking_date = models.DateField(default=date.today)
	status = models.CharField(max_length=30,default='completed')
	adult = models.CharField(max_length=30,default='')
	child = models.CharField(max_length=30,default='')

	class Meta:
		db_table = 'booking'



class Payment(models.Model):
	login = models.ForeignKey(Login,on_delete=models.CASCADE)
	booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
	payment_mode = models.CharField(max_length=40)
	amount = models.BigIntegerField()
	payment_date = models.DateField(default=date.today)

	class Meta:
		db_table = 'payment'


class Date(models.Model):
	ddate = models.DateField()
	tdate = models.DateField()
	plan = models.ForeignKey(Plan,on_delete=models.CASCADE,default='')


	class Meta:
		db_table = 'date'

