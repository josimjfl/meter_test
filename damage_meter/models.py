from django.db import models

# Create your models here.


class PurchaseOrder(models.Model):
	purchase_order = models.CharField(max_length=100)
	remark = models.CharField(max_length=150, blank=True, null=True)		

	def __str__(self):
		return self.purchase_order