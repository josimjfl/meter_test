from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Sum, Avg, F, Window, RowRange
from accounts.decorators import role_required
from django.utils.decorators import method_decorator  #for class based view
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
import datetime
from django.http import JsonResponse
today=datetime.date.today().strftime("%d-%m-%Y")


@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class AddItem(View):
    def get(self, *args, **kwargs):
        try:
            last_data= Balance.objects.filter(office=self.request.user.office).latest('id')
        except Balance.DoesNotExist:
            last_data = None
        try:
            item = Item.objects.all()
        except Item.DoesNotExist:
            item = None
        return render(self.request,'balance_reg/add_item.html', {'last_data':last_data, 'item':item})

    def post(self, *args, **kwargs):
        date_start =self.request.POST.get('date_start')
        ticket_no =self.request.POST.get('ticket_no')
        referance_name =self.request.POST.get('referance_name')
        j_1 = self.request.POST.get('J-1')
        j_2 = self.request.POST.get('J-2')
        j_3 = self.request.POST.get('J-3')
        j_4 = self.request.POST.get('J-4')
        j_31 = self.request.POST.get('J-31')
        j_39 = self.request.POST.get('J-39')
        j_16 = self.request.POST.get('J-16')

        # if any problem to continue db will not change any part of data for transaction.atomic()
        with transaction.atomic():
            if j_1 != "":
                Balance.objects.create(office= self.request.user.office, item=Item.objects.get(item_no="J-1") ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_1, created_by=self.request.user)

            if j_2 !="":
                Balance.objects.create(office= self.request.user.office, item=Item.objects.get(item_no="J-2") ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_2, created_by=self.request.user)  

            if j_3 !="":
                Balance.objects.create(office= self.request.user.office, item=Item.objects.get(item_no="J-3") ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_3, created_by=self.request.user)

            if j_4 !="":
                Balance.objects.create(office= self.request.user.office, item=Item.objects.get(item_no="J-4") ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_4, created_by=self.request.user)

            if j_31 != "":
                SealBalance.objects.create(office= self.request.user.office, item="J-31" ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_31, created_by=self.request.user)

            if j_39 !="":
                Balance.objects.create(office= self.request.user.office, item=Item.objects.get(item_no="J-39") ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_39, created_by=self.request.user)

            if j_16 !="":
                Balance.objects.create(office= self.request.user.office, item=Item.objects.get(item_no="J-16") ,date_start=date_start,ticket_no=ticket_no,referance_name=referance_name,credit_qty=j_16, created_by=self.request.user)

        try:
            item = Item.objects.all()
        except Item.DoesNotExist:
            item = None
        messages.success(self.request, 'Successfully Accepted!')
        last_data= Balance.objects.filter(office=self.request.user.office).latest('id')
        return render(self.request,'balance_reg/add_item.html', {'last_data':last_data, 'item':item})



@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class IssueItem(View):
    def get(self, *args, **kwargs):
        try:
            obj= Balance.objects.filter(office=self.request.user.office).latest('id')
        except Balance.DoesNotExist:
            obj = None

        try:
            seal = SealBalance.objects.filter(office=self.request.user.office).latest('id')
        except SealBalance.DoesNotExist:
            seal = None
        item = Item.objects.all()
        return render(self.request,'balance_reg/issue_item.html', {'obj':obj, 'item':item, 'seal':seal})

    def post(self, *args, **kwargs):
        meter = Balance()
        seal = SealBalance()
        #Get data
        office= self.request.user.office
        store_return_ticket = self.request.POST.get('store_return_ticket')
        name =self.request.POST.get('name')
        sl_start =self.request.POST.get('sl_start')
        sl_end =self.request.POST.get('sl_end')
        date_start =self.request.POST.get('date_start')
        date_end =self.request.POST.get('date_start')
        total_seal =self.request.POST.get('j31total')
        debit_qty =self.request.POST.get('debit_qty')
        remark = self.request.POST.get('remark')
        created_by=self.request.user
        item_no =self.request.POST.get('item_no')

        # if any problem to continue db will not change any part of data for transaction.atomic()
        with transaction.atomic():        
            #if item is only j-31 save to j-31
            if item_no == "J-31":
                if store_return_ticket != "":
                    SealBalance.objects.create(office= self.request.user.office, item="J-31",date_start=date_start, date_end=date_end, store_return_ticket=store_return_ticket, remark=remark, debit_qty=debit_qty, created_by=self.request.user)
                    msg='Successfully Return only Seal to Store!'
                else:
                    SealBalance.objects.create(office= self.request.user.office, item="J-31",date_start=date_start, date_end=date_end, sl_start=sl_start, sl_end=sl_end,remark="J-31", debit_qty=debit_qty, created_by=self.request.user)
                    msg='Successfully Accepted only Seal as Register!'
            else:
                item = Item.objects.get(item_no=item_no)

                if store_return_ticket != "":
                    Balance.objects.create(office= self.request.user.office, item=item ,date_start=date_start, date_end=date_end,store_return_ticket=store_return_ticket, debit_qty=debit_qty, created_by=self.request.user)
                    #seal save
                    SealBalance.objects.create(office= self.request.user.office, item="J-31",date_start=date_start, date_end=date_end,store_return_ticket=store_return_ticket, remark=item_no, debit_qty=debit_qty, created_by=self.request.user)
                    msg='Successfully Accepted as Store return!'
                else:
                    Balance.objects.create(office= self.request.user.office, item=item ,date_start=date_start, date_end=date_end, sl_start=sl_start, sl_end=sl_end, debit_qty=debit_qty, created_by=self.request.user)
                    #Seal save
                    SealBalance.objects.create(office= self.request.user.office, item="J-31",date_start=date_start, date_end=date_end, sl_start=sl_start, sl_end=sl_end, remark=item_no, debit_qty=debit_qty, created_by=self.request.user)
                    msg='Successfully Accepted as Register Issue.!'
            data = {'error': False, 'msg': msg, 'sl_end':sl_end}
            return JsonResponse(data, safe=False)




class BalanceView(View):
    def get(self, *args, **kwargs):
        #Get last query
        try:
            obj= Balance.objects.filter(office=self.request.user.office).latest('id')
        except Balance.DoesNotExist:
            obj = None
        try:
            seal = SealBalance.objects.filter(office=self.request.user.office).latest('id')
        except SealBalance.DoesNotExist:
            seal = None

        item = Item.objects.all()
        return render(self.request,'balance_reg/balance_index.html', {'obj':obj, 'item':item, 'seal':seal})
        
    def post(self, *args, **kwargs):
        item_no = self.request.POST.get('item_no')
        from_date = self.request.POST.get('from_date')
        to_date = self.request.POST.get('to_date')
        #select seal or meter model
        if item_no == "J-31":
            Res_office = SealBalance.objects.filter(office=self.request.user.office, item="J-31")
        else:
            get_item = Item.objects.get(item_no=item_no)
            Res_office = Balance.objects.filter(office=self.request.user.office, item=get_item)


        if from_date !=None and to_date != None:
            Res = Res_office.filter(date_start__range=[from_date,to_date]).order_by('date_start')
            result = Res.annotate(
            total=Window(
                expression=Sum('credit_qty'),
                order_by=F('date_start').asc(),
                frame=RowRange(end=0)
                ),
            total2 =Window(
                expression=Sum('debit_qty'),
                order_by=F('date_start').asc(),
                frame=RowRange(end=0)
                )
            ).annotate(some_suitable_name_here= F('credit_qty')- F('total2') - F('total'))
        elif  item_no != None:
            Res = Res_office.order_by('date_start')
            #For dynamic sum at every line in lazer 
            result = Res_office.annotate(
            total=Window(
                expression=Sum('credit_qty'),
                order_by=F('date_start').asc(),
                frame=RowRange(end=0)
                ),
            total2 =Window(
                expression=Sum('debit_qty'),
                order_by=F('date_start').asc(),
                frame=RowRange(end=0)
                )
            ).annotate(some_suitable_name_here= F('credit_qty')- F('total2') - F('total'))
        else:
            pass



        obj = Res.order_by('date_start')
        #get total credit
        total_credit_qty=obj.aggregate(s=Sum('credit_qty'))['s']
        if total_credit_qty != None:
            total_credit_quantity=round(float(total_credit_qty),2)
        else:
            total_credit_quantity=0

        #get total debit
        total_debit_qty=obj.aggregate(s=Sum('debit_qty'))['s']
        if total_debit_qty != None:
            total_debit_quantity=round(float(total_debit_qty),2)
        else:
            total_debit_quantity = 0

        #balance
        balance_in_hand =total_credit_quantity - total_debit_quantity


        obj_result_compbined = zip(obj, result)
        return render(self.request, 'balance_reg/balance.html', 
            {
            'item_no':item_no,
            'from_date':from_date,
            'to_date':to_date,
            'total_debit_quantity':total_debit_quantity,
            'total_credit_quantity':total_credit_quantity,
            'balance_in_hand':balance_in_hand,
            'obj_result_compbined':obj_result_compbined,
            })


def balance_summary_view(request):
    #J-31 balance summary
    Seal_BL = SealBalance.objects.filter(office=request.user.office)
    total_credit_qty=Seal_BL.filter(item="J-31").aggregate(s=Sum('credit_qty'))['s']
    if total_credit_qty == None:
        total_credit_qty=0
    total_debit_qty=Seal_BL.filter(item="J-31").aggregate(s=Sum('debit_qty'))['s']
    if total_debit_qty==None:
        total_debit_qty=0
    seal_bl_sum = total_credit_qty - total_debit_qty


    #All item total balance summary   
    Res_office = Balance.objects.filter(office=request.user.office)
    date = Res_office.latest('id')
    item = Item.objects.all()
    obj = []
    item_box = []
    for x in item:
        total_credit_qty=Res_office.filter(item=x.id).aggregate(s=Sum('credit_qty'))['s']
        if total_credit_qty == None:
            total_credit_qty=0
        total_debit_qty=Res_office.filter(item=x.id).aggregate(s=Sum('debit_qty'))['s']
        if total_debit_qty==None:
            total_debit_qty=0
        balance = total_credit_qty - total_debit_qty

        # Appending new data
        new_data = {'item': x.item_no, 'balance': balance}
        obj.append(new_data)
 
    return render(request, 'balance_reg/balance_summary.html', {'balance':balance, 'obj':obj, 'seal_bl_sum':seal_bl_sum, 'date':date })

def last_balance(request):
    item_no = request.GET.get('item_no')
    if item_no == "J-31":
        last_bl = SealBalance.objects.filter(office=request.user.office, item=item_no).latest('id');
    else:
        item = Item.objects.get(item_no=item_no)
        last_bl = Balance.objects.filter(office=request.user.office, item=item).latest('id');
    data = {'last_bl':last_bl.sl_end, }
    return JsonResponse(data, safe=False)

# Django Drag and drop sort item
def item_list(request):
    items = Item.objects.all().order_by('order')
    return render(request, 'balance_reg/item_list.html', {'items': items})



@login_required
@role_required(['admin', 'MT', 'MTS'])          #For user Group test
def update_item_order(request):
    if request.method == 'POST':
        item_order = request.POST.getlist('item_order[]')
        for index, item_id in enumerate(item_order):
            item = Item.objects.get(pk=item_id)
            item.order = index
            item.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})