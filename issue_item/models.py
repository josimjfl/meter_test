from django.db import models
from balance_reg.models import Item
from accounts.models import Office, default_office, CustomUser as User


class IssueItem(models.Model):
	office = models.ForeignKey(Office, on_delete=models.CASCADE, default=default_office)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	serial = models.CharField(max_length=20, null=True, blank=True)
	cmo = models.CharField(max_length=20, null=True, blank=True)
	received_by = models.CharField(max_length=100, null=True, blank=True)
	meter_no = models.CharField(max_length=100, null=True, blank=True)
	reading = models.CharField(max_length=50, null=True, blank=True)
	main_seal = models.CharField(max_length=50, null=True, blank=True)
	body_seal1 = models.CharField(max_length=50, null=True, blank=True)
	body_seal2 = models.CharField(max_length=50, null=True, blank=True)
	mfg = models.CharField(max_length=50, null=True, blank=True)
	total_j31 = models.IntegerField(default=0)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="issue_created_by")
	created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="issue_updated_by" )
	updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

	class Meta:
		ordering = ['-id']


	def __str__(self):
		#title=str(self.pk)
		title = 'id-' + str(self.pk)+', Item-' + str(self.item) +', Meter-'+ str(self.meter_no) +', Seal-'+str(self.main_seal)+ ', Date-'+str(self.created_date)
		return title





class SealIssue(models.Model):
	office = models.ForeignKey(Office, on_delete=models.CASCADE, default=default_office)
	item = models.CharField(max_length=20, null=True, blank=True, default="J-31")
	cmo = models.CharField(max_length=20, null=True, blank=True)
	book = models.CharField(max_length=10, null=True, blank=True)
	account = models.CharField(max_length=10, null=True, blank=True)
	received_by = models.CharField(max_length=100, null=True, blank=True)
	main_seal = models.CharField(max_length=50, null=True, blank=True)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seal_issue_created_by")
	created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seal_issue_updated_by" )
	updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
	
	class Meta:
		ordering = ['-id']

	def __str__(self):
		#title=str(self.pk)
		title = 'id-' + str(self.pk)+', Item-' + str(self.item) +', Seal-'+str(self.main_seal)+ ', Date-'+str(self.created_date)
		return title