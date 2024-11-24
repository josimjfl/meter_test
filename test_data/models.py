from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import Office, default_office, CustomUser as User
from balance_reg.models import Item

import datetime
today=datetime.date.today().strftime("%Y-%m-%d")



class uploads(models.Model):
    fullname = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    url = models.TextField(null=True, default=" ")


test_choice = (
	('BREB', 'BREB'),
	('PBS', 'PBS'),
	)

class Manufacturer(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	kh = models.CharField(max_length=5, blank=True, null=True)
	meter_class = models.CharField(max_length=5, blank=True, null=True)
	item_no = models.ForeignKey(Item, on_delete=models.CASCADE)
	test_to = models.TextField(blank=True, null=True, choices=test_choice)
	meter_type = models.CharField(max_length=20, blank=True, null=True)
	LL_TA = models.CharField(max_length=5, default=1)
	FL_TA = models.CharField(max_length=5, default=10)
	LL_rev = models.CharField(max_length=5, default=2)
	FL_rev = models.CharField(max_length=5, default=10)
	standerd_rev_req_ll = models.CharField(max_length=10, blank=True, null=True)
	standerd_rev_req_fl = models.CharField(max_length=10, blank=True, null=True)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order']

	def __str__(self):
		return self.name


remark_choice = (
	('ব্যবহার উপযোগী।', 'ব্যবহার উপযোগী।'),
	('ব্যবহার অনুপযোগী।', 'ব্যবহার অনুপযোগী।'),
	('পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।', 'পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।'),
	)


class Results(models.Model):
	office = models.ForeignKey(Office, on_delete=models.CASCADE, default=default_office)
	name = models.CharField(max_length=100)
	items = models.ManyToManyField(Item)
	details = models.CharField(max_length=1000, blank=True, null=True)
	remark = models.TextField(blank=True, null=True, choices=remark_choice)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order']
		
	# To see ManyToMany field in django admin
	def get_items(self):
		return "\n".join([p.item_no for p in self.items.all()])

	def __str__(self):
		return self.name


class Test_Data(models.Model):
	office = models.ForeignKey(Office, on_delete=models.CASCADE, default=default_office)
	tested_meter_no = models.CharField(max_length=20, blank=True, null=True)
	reading_as_found = models.CharField(max_length=20, default="x")
	reading_as_left = models.CharField(max_length=20, default="x")
	multiplier = models.CharField(max_length=20, default=1)
	cmo = models.CharField(max_length=20, blank=True, null=True)
	book = models.CharField(max_length=3, blank=True, null=True)
	account = models.CharField(max_length=4, blank=True, null=True)
	manufacturer = models.CharField(max_length=30, blank=True, null=True)
	meter_class = models.CharField(max_length=5, blank=True, null=True)
	meter_item = models.CharField(max_length=100, blank=True, null=True)
	kh = models.CharField(max_length=5, blank=True, null=True)
	#Results
	result = models.PositiveIntegerField(default=0)
	LL_TA = models.CharField(max_length=5, default=1)
	FL_TA = models.CharField(max_length=5, default=10)
	LL_rev = models.CharField(max_length=5, default=2)
	FL_rev = models.CharField(max_length=5, default=10)
	as_found_ll = models.CharField(max_length=10, blank=True, null=True)
	as_found_fl = models.CharField(max_length=10, blank=True, null=True)
	percent_found_ll = models.CharField(max_length=10, blank=True, null=True)
	percent_found_fl = models.CharField(max_length=10, blank=True, null=True)	
	error_ll = models.CharField(max_length=10, blank=True, null=True)
	error_fl = models.CharField(max_length=10, blank=True, null=True)
	as_left_ll = models.CharField(max_length=10, blank=True, null=True)
	as_left_fl = models.CharField(max_length=10, blank=True, null=True)
	percent_left_ll = models.CharField(max_length=10, blank=True, null=True)
	percent_left_fl = models.CharField(max_length=10, blank=True, null=True)
	error_left_ll = models.CharField(max_length=10, blank=True, null=True)
	error_left_fl = models.CharField(max_length=10, blank=True, null=True)
	standerd_rev_req_ll = models.CharField(max_length=10, blank=True, null=True)
	standerd_rev_req_fl = models.CharField(max_length=10, blank=True, null=True)
	#Inventory
	terminal_seal= models.CharField(max_length=50, blank=True, null=True)
	terminal_seal_no = models.CharField(max_length=20, null=True, blank=True)
	terminal_seal_missing = models.CharField(max_length=100, null=True, blank=True)
	body_seal= models.CharField(max_length=50, blank=True, null=True)
	glass_cover = models.CharField(max_length=100, null=True, blank=True)
	test_clip = models.CharField(max_length=100, null=True, blank=True)
	remove_cause = models.CharField(max_length=255, blank=True, null=True)
	remove_date = models.DateField(null=True, blank=True)
	install_date = models.DateField(null=True, blank=True)
	#Comments
	comments = models.TextField(default="মিটারটি ভালো আছে।", max_length=200, blank=True, null=True)
	remark = models.CharField(max_length=200, blank=True, null=True)
	cmo_type = models.CharField(max_length=50, blank=True, null=True)
	purchase_order =  models.CharField(max_length=100, default="-")
	#Authorizarion
	created_by = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE, related_name="td_created_by")
	created_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
	updated_by = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE, related_name="td_updated_by")
	updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
	checked_by = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE, related_name="checked_by")
	checked_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
	counter_sign_by = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE, related_name="counter_sign_by")
	counter_sign_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
	print_counter = models.IntegerField(null=True, blank=True, default=0)
	received_by = models.ForeignKey(User, null=True, blank=True,  default=None, on_delete=models.CASCADE, related_name="received_by")
	received_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
	


	def __str__(self):
		return self.tested_meter_no

	def summary(self):
		return self.body[:30]



