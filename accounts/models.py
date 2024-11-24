
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
#For Auto create OfficeEmp Model data
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone



def default_pbs():
    return Pbs.objects.get_or_create(id=1)[0]


def default_office():
    return Office.objects.get_or_create(id=1)[0]


class Pbs(models.Model):
	pbs_code = models.CharField(max_length=10, null=True, blank=True, default="0")
	pbs_name = models.CharField(max_length=150, null=True, blank=True, default="default_pbs")
	updated_by = models.CharField(max_length=100, blank=True, null=True)


	def __str__(self):
		title = str(self.pbs_code) +' '+str(self.pbs_name)
		return title


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
	updated_by = models.CharField(max_length=100, blank=True, null=True)


	def __str__(self):
		title = str(self.office_code) +' '+ str(self.office_name) +' '+ str(self.pbs)
		return title



def today():
    return timezone.now().date()


class Standard_Meter(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, default=default_office, blank=True, null=True)
    std_serial = models.CharField(max_length=20, blank=True, null=True)
    std_name = models.CharField(max_length=20, blank=True, null=True)
    std_kh = models.CharField(max_length=5, blank=True, null=True)
    from_date = models.DateField(auto_now_add=False, default=today)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.std_serial} - ({self.office})"




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
        ('DGM', 'DGM'),
        ('BS', 'BS'),
        ('BA', 'BA'),
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
    date = models.DateField(auto_now_add=False, auto_now=False, default=today)
    sign_image = models.ImageField(upload_to='images/', null=True, blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    password_changed_at = models.DateTimeField(auto_now=True)  # Auto-updates on save

    def save(self, *args, **kwargs):
        # Track password change by comparing hashed password
        if self.pk:
            original_user = CustomUser.objects.get(pk=self.pk)
            if original_user.password != self.password:
                # Password has changed
                self.password_changed_at = timezone.now()
        # Ensure the password field is being hashed correctly before saving
        super().save(*args, **kwargs)




from django.db import models
from django.utils import timezone

class OfficeEmp(models.Model):
    office = models.OneToOneField(Office, on_delete=models.CASCADE)
    tested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_tested_by")
    checked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_checked_by")
    counter_sign_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_counter_sign_by")
    received_by =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="office_received_by")
    standered_meter = models.ForeignKey(Standard_Meter, on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Check if request is available and assign current user
        if 'request' in kwargs:
            self.updated_by = kwargs.pop('request').user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.standered_meter) if self.standered_meter else "No Standard Meter"

