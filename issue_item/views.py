from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import *
from accounts.models import CustomUser
from test_data.models import Manufacturer
from balance_reg.models import *
from django.db import transaction
from django.db.models import F, Sum
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator  #for class based view
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required    #for def require view
import json
from datetime import date
today = date.today()

from django.contrib.auth import get_user_model




@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')  #only for reqired person can see
class IssueItemView(View):
    def get(self, *args, **kwargs):
    	item = Item.objects.all()
    	mfg = Manufacturer.objects.all()
    	employee = CustomUser.objects.filter(office=self.request.user.office)
    	try:
    		last_issue = IssueItem.objects.filter(office=self.request.user.office).latest('id')
    	except IssueItem.DoesNotExist:
    		last_issue = None
    	return render(self.request, 'issue_item/issue_item.html', {'item':item,'mfg':mfg, 'employee':employee, 'last_issue':last_issue})



@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class IssueSealView(View):
    def get(self, *args, **kwargs):
    	item = Item.objects.all()
    	mfg = Manufacturer.objects.all()
    	employee = CustomUser.objects.filter(office=self.request.user.office)
    	try:
    		last_issue = SealIssue.objects.filter(office=self.request.user.office).latest('id')
    	except SealIssue.DoesNotExist:
    		last_issue = None
    	return render(self.request, 'issue_item/issue_seal.html', {'item':item, 'mfg':mfg, 'employee':employee, 'last_issue':last_issue})


@login_required
@role_required(['admin', 'MT', 'MTS']) 			#For user Group test
def issue_ajax(request):
	if request.method == 'GET':
		data = {"message":"Thanks"}
		return JsonResponse(data)

	if request.method == 'POST':
		meter_no = request.POST.get('meter_no')
		reading = request.POST.get('reading')
		main_seal = request.POST.get('main_seal')
		book = request.POST.get('book')
		account = request.POST.get('account')
		cmo = request.POST.get('cmo')
		body_seal1 = request.POST.get('body_seal1')
		body_seal2 = request.POST.get('body_seal2')
		total_j31 = request.POST.get('total_seal')
		received_by = request.POST.get('received_by')
		item_no = request.POST.get('item_no')
		manufacturer = request.POST.get('manufacturer')
		req_user = request.user
		seal = "J-31"

		if total_j31 == None:
			total_j31 = 0

		# if any problem to continue db will not change any part of data for transaction.atomic()
		with transaction.atomic():
			if item_no != "J-31" and item_no != '':
				item = Item.objects.get(item_no=item_no)
				#check item balance
				item_bl = Balance.objects.filter(item=item).aggregate(total=Sum(F('credit_qty') - F('debit_qty')))['total']
				if item_bl == None:
					item_bl = 0
				#check seal balance
				seal_bl = SealBalance.objects.filter(item=seal).aggregate(total=Sum(F('credit_qty') - F('debit_qty')))['total']
				if seal_bl == None:
					seal_bl = 0

				if item_bl >= 1 and seal_bl >= float(total_j31):
					#add to issue model
					issue = IssueItem.objects.create(
						office = request.user.office,
						item = item,
						meter_no=meter_no, 
						reading=reading,
						main_seal=main_seal,
						cmo=cmo,
						body_seal1=body_seal1,
						body_seal2=body_seal2,
						received_by=received_by,
						mfg = manufacturer,
						total_j31 = total_j31,
						created_by = req_user,
						updated_by = req_user,
						)
					#add all balance in one day.
					created = Balance.objects.get_or_create(office=request.user.office, item=item, date_start=today, store_return_ticket="")
					created2 = SealBalance.objects.get_or_create(office=request.user.office, item=seal, date_start=today, store_return_ticket="")
					Balance.objects.filter(office=request.user.office, date_start=today, item=item, store_return_ticket="").update(debit_qty=F('debit_qty')+1, sl_end=issue.id, created_by=req_user, updated_by=req_user)
					SealBalance.objects.filter(office=request.user.office, date_start=today, item=seal, store_return_ticket="").update(debit_qty=F('debit_qty')+total_j31, sl_end=issue.id, created_by=req_user, updated_by=req_user)
					data = {
							"id":issue.id, 
							"meter_no":issue.meter_no, 
							"reading":issue.reading,
							"cmo":issue.cmo,
							"main_seal":issue.main_seal,
							"total_j31":total_j31,
							"received_by":issue.received_by,
							"body_seal1":body_seal1,
							"body_seal2":body_seal2,
							"item_no":item_no,
							"status":"successfull",
							"message":"Post Complete",
						}					
				else:
					data = {"status":"failed", "message":"Failed, Balance nill or item not found."}

					return JsonResponse(data, safe=False)



			elif item_no == "J-31":
				#check balance  office
				item_bl = SealBalance.objects.aggregate(total=Sum(F('credit_qty') - F('debit_qty')))['total']
				if item_bl == None:
					item_bl=0

				if item_bl >= 1:
					issue = SealIssue.objects.create(
						office = request.user.office,
						book=book, 
						account=account,
						main_seal=main_seal,
						cmo=cmo,
						received_by=received_by,
						item = item_no,
						created_by = req_user,
						updated_by = req_user,		
						)

					#add all balance in one day. check data have or not. if not create the day and update the balance data
					created = SealBalance.objects.get_or_create(office=request.user.office, item=seal, date_start=today, store_return_ticket="")
					SealBalance.objects.filter(office=request.user.office, date_start=today, item=seal, store_return_ticket="").update(debit_qty=F('debit_qty')+1, sl_end=issue.id, created_by=req_user, updated_by=req_user)
					data = {
							"id":issue.id, 
							"book":issue.book, 
							"account":issue.account,
							"cmo":issue.cmo,
							"main_seal":issue.main_seal,
							"total_j31":total_j31,
							"received_by":issue.received_by,
							"item_no":item_no,
							"status":"successfull",
							"message":"Post Complete",
						}
				else:
					data = {"status":"failed", "message":"Failed, Balance not sufficient or item not found."}
					return JsonResponse(data, safe=False)


			else:
				data = {"status":"failed", "message":"Failed, item not found."}
				return JsonResponse(data, safe=False)

		return JsonResponse(data, safe=False)



@login_required
@role_required(['admin', 'MT', 'MTS']) 			#For user Group test
def update_issue_ajax(request):
	if request.method == 'GET':
		data = {"message":"Thanks"}
		return JsonResponse(data)

	if request.method == 'POST':
		meter_id = request.POST.get('meter_id')
		meter_no = request.POST.get('meter_no')
		reading = request.POST.get('reading')
		main_seal = request.POST.get('main_seal')
		cmo = request.POST.get('cmo')
		body_seal1 = request.POST.get('body_seal1')
		body_seal2 = request.POST.get('body_seal2')
		total_j31 = request.POST.get('total_seal')
		received_by = request.POST.get('received_by')
		manufacturer = request.POST.get('manufacturer')
		book = request.POST.get('book')
		account = request.POST.get('account')
		item_no = request.POST.get('item_no')
		seal = "J-31"
		if total_j31 == None:
			total_j31 = 0

		# if any problem to continue db will not change any part of data for transaction.atomic()
		with transaction.atomic():
			if item_no != "J-31" and item_no != '':
				item = Item.objects.get(item_no=item_no)
				#check balance
				item_bl = Balance.objects.filter(item=item).aggregate(total=Sum(F('credit_qty') - F('debit_qty')))['total']
				if item_bl == None:
					item_bl = 0

				seal_bl = SealBalance.objects.filter(item=seal).aggregate(total=Sum(F('credit_qty') - F('debit_qty')))['total']
				if seal_bl == None:
					seal_bl = 0

				if item_bl >= 1 and seal_bl >= float(total_j31):
					#add to issue model
					issue = IssueItem.objects.get(id=meter_id)
					if issue.total_j31 != total_j31:
						SealBalance.objects.filter(office=request.user.office, date_start=issue.created_date, item=seal, store_return_ticket="").update(debit_qty=F('debit_qty')-issue.total_j31, sl_end=issue.id)
						SealBalance.objects.filter(office=request.user.office, date_start=issue.created_date, item=seal, store_return_ticket="").update(debit_qty=F('debit_qty')+total_j31, sl_end=issue.id)
					IssueItem.objects.filter(id=meter_id).update(
						meter_no=meter_no, 
						reading=reading,
						main_seal=main_seal,
						cmo=cmo,
						body_seal1=body_seal1,
						body_seal2=body_seal2,
						received_by=received_by,
						item = item,
						mfg = manufacturer,
						total_j31 = total_j31,
						)
					#add all balance in one day.
				else:
					data = {"status":"failed", "message":"Failed, item not found."}
					return JsonResponse(data, safe=False)



			elif item_no == "J-31":
				#check balance				
				seal_bl = SealBalance.objects.filter(item=seal).aggregate(total=Sum(F('credit_qty') - F('debit_qty')))['total']
				if seal_bl == None:
					seal_bl = 0

				if seal_bl >= 1:
					issue = SealIssue.objects.filter(id=meter_id).update(
						book=book, 
						account=account,
						main_seal=main_seal,
						cmo=cmo,
						received_by=received_by,
						item = item_no,			
						)
					#seal balance will not be changed.
				else:
					data = {"status":"failed", "message":"Failed, Balance is not sufficient."}
					return JsonResponse(data, safe=False)


			else:
				data = {"status":"failed", "message":"Failed, item not found."}
				return JsonResponse(data, safe=False)

		data = {"status":"successfull",  "message":"Successfully Updated",}
		return JsonResponse(data, safe=False)



@login_required
@role_required(['admin', 'MT', 'MTS']) 
def meter_issue_list(request):
	item = Item.objects.all()
	try:
		item_list=IssueItem.objects.filter(office=request.user.office)
	except IssueItem.DoesNotExist:
		item_list = None
	paginator = Paginator(item_list, 20) # Show 20 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	#date = datetime.date.today().strftime("%d-%m-%Y")
	mfg = Manufacturer.objects.all()
	employee = CustomUser.objects.filter(office=request.user.office)
	return render(request, 'issue_item/meter_issue_list.html', {'item_list':item_list, 'mfg':mfg, 'employee':employee, 'page_obj':page_obj, 'item':item})



@login_required
@role_required(['admin', 'MT', 'MTS']) 
def seal_issue_list(request):
	try:
		seal_list=SealIssue.objects.filter(office=request.user.office)
	except SealIssue.DoesNotExist:
		seal_list = None
	paginator = Paginator(seal_list, 20) # Show 20 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	#date = datetime.date.today().strftime("%d-%m-%Y")
	employee = CustomUser.objects.filter(office=request.user.office)
	return render(request, 'issue_item/seal_issue_list.html', {'seal_list':seal_list, 'employee':employee, 'page_obj':page_obj})
