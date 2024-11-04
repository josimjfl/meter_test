
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
#For Auto create OfficeEmp Model data
from django.dispatch import receiver
from django.db.models.signals import post_save



def get_pbs():
    return Pbs.objects.get_or_create(id=1)


def get_office():
	return Office.objects.get_or_create(id=1)


class Pbs(models.Model):
	pbs_code = models.CharField(max_length=10, null=True, blank=True, default="0")
	pbs_name = models.CharField(max_length=150, null=True, blank=True, default="default_pbs")


	def __str__(self):
		title = str(self.pbs_code) +' '+str(self.pbs_name)
		return title


class Standard_Meter(models.Model):
	pbs = models.ForeignKey(Pbs, on_delete=models.CASCADE, default=get_office, blank=True, null=True)
	std_serial = models.CharField(max_length=20, blank=True, null=True)
	std_name = models.CharField(max_length=20, blank=True, null=True)
	std_kh = models.CharField(max_length=5, blank=True, null=True)
	from_date=models.DateField(auto_now_add=False,auto_now=False,default=today)

	def __str__(self):
		return self.std_serial


item_choice=[
	('head_quater','HQ'),
	('zonal','ZO'),
	('sub_zonal','SZO'),
	]



class Office(models.Model):
	pbs = models.ForeignKey(Pbs, on_delete=models.CASCADE, blank=True, null=True)
	office_name =  models.CharField(max_length=255, null=True, blank=True)
	office_code = models.CharField(max_length=10, null=True, default="0")
	catagory = models.CharField(max_length=150, blank=True, null=True, choices= item_choice)


	def __str__(self):
		title = str(self.office_code) +' '+ str(self.office_name) +' '+ str(self.pbs)
		return title

class Designation(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    details = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
    	return self.title


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('MT', 'MT'),
        ('MTS', 'MTS'),
        ('IT', 'IT'),
        ('AGM', 'AGM'),
        ('BS', 'BS'),
        ('JE', 'JE'),
        ('LT', 'LT'),
        ('LM', 'LM'),
        ('user', 'User'),
    )
    username = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=30, unique=True, blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)
    training_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    date=models.DateField(auto_now_add=False,auto_now=False,default=today)
    sign_image = models.ImageField(upload_to='images/', null=True, blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)




class OfficeEmp(models.Model):
	office = models.OneToOneField(Office, on_delete=models.CASCADE)
	tested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_tested_by")
	checked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_checked_by")
	counter_sign_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_counter_sign_by")
	received_by = models.CharField(max_length=100, blank=True, null=True)
	standered_meter = models.ForeignKey(Standard_Meter, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.standered_meter.std_serial

"""
	#To auto create new profile when add new user.
	@receiver(post_save, sender=CustomUser)
	def OfficeEmp_create(sender, instance=None, created=False, **kwargs):
	    if created:
	    	OfficeEmp.objects.get_or_create(office=user.office)


	def __str__(self):
		return self.office.office_name
"""