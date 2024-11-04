from django.db import models
from accounts.models import Office, get_office, CustomUser as User

import datetime
today=datetime.date.today().strftime("%Y-%m-%d")



class Item(models.Model):
	item_no = models.CharField(max_length=100, unique=True)
	details = models.CharField(max_length=255, blank = True)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order']

	def __str__(self):
		return str(self.item_no)


class Balance(models.Model):
	office = models.ForeignKey(Office, on_delete=models.CASCADE, default=get_office)
	item = models.ForeignKey(Item, on_delete = models.CASCADE, blank=True)
	sl_start = models.CharField(max_length=10, blank=True, null=True)
	sl_end = models.CharField(max_length=10, blank=True, null=True)
	date_start = models.DateField(auto_now_add=False, auto_now=False)
	date_end = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	store_return_ticket = models.CharField(max_length=50, blank=True, null=True)
	ticket_no = models.CharField(max_length=50, blank=True, null=True)
	referance_name = models.CharField(max_length=50, blank=True, null=True)
	remark = models.CharField(max_length=200, blank=True, null=True)
	debit_qty = models.IntegerField(default=0)
	credit_qty = models.IntegerField(default=0)
	balance = models.IntegerField(default=0)
	#user
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="balance_created_by")
	created_date = models.DateField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="balance_updated_by")
	updated_date = models.DateField(auto_now=True, null=True, blank=True)

	class Meta:
		ordering = ['date_start']

	def __str__(self):
		title = str(self.id) +'- Date-'+ str(self.date_start) +'- Item-'+ str(self.item.item_no)
		return title



class SealBalance(models.Model):
	office = models.ForeignKey(Office, on_delete=models.CASCADE, default=get_office)
	item = models.CharField(max_length=10, blank=True, null=True, default="J-31")
	sl_start = models.CharField(max_length=10, blank=True, null=True)
	sl_end = models.CharField(max_length=10, blank=True, null=True)
	date_start = models.DateField(auto_now_add=False, auto_now=False)
	date_end = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	store_return_ticket = models.CharField(max_length=50, blank=True, null=True)
	ticket_no = models.CharField(max_length=50, blank=True, null=True)
	referance_name = models.CharField(max_length=50, blank=True, null=True)
	remark = models.CharField(max_length=200, blank=True, null=True)
	debit_qty = models.IntegerField(default=0)
	credit_qty = models.IntegerField(default=0)
	balance = models.IntegerField(default=0)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="seal_balance_created_by")
	created_date = models.DateField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="seal_balance_updated_by")
	updated_date = models.DateField(auto_now=True, null=True, blank=True)

	class Meta:
		ordering = ['date_start']
		
	def __str__(self):
		title = str(self.id) +'- Date-'+ str(self.date_start) +'- Item-'+ str(self.remark)
		return title

