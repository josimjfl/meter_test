from django.shortcuts import render
from test_data.models import Test_Data
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.core import paginator
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User


from accounts.decorators import role_required


@login_required
@role_required(['admin'])
def admin_dashboard(request):
    profile = CustomUser.objects.all().order_by('-id')
    return render(request, "dashboard/admin_dashboard.html", {'profile':profile})


@login_required
@role_required(['admin', 'user', 'IT'])          #For user Group test    
def user_dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    return render(request, "dashboard/user_dashboard.html", {'profile':profile})


@login_required
@role_required(['admin', 'LT', 'LM', 'JE', 'IT'])          #For user Group test    
def dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    return render(request, "dashboard/lm_dashboard.html", {'profile':profile})



@login_required
@role_required(['admin', 'LT', 'LM', 'JE'])          #For user Group test    
def lm_dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    return render(request, "dashboard/lm_dashboard.html", {'profile':profile})



@login_required
@role_required(['admin', 'IT'])          #For user Group test    
def it_dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    return render(request, "dashboard/it_dashboard.html", {'profile':profile})



@login_required
@role_required(['admin', 'MT', 'MTS']) 			#For user Group test	
def mt_dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    return render(request, "dashboard/mt_dashboard.html", {'profile':profile})




@login_required
@role_required(['admin', 'MTS', 'MT']) 			#For user Group test
def mts_dashboard(request):
    if request.method=="GET":
        page = int(request.GET.get('page', 1))
        posts = Test_Data.objects.filter(office =request.user.office, checked_by__isnull=True).order_by('-id')
        panding_qty = Test_Data.objects.filter(office =request.user.office, checked_by__isnull=True).count()
        profile= CustomUser.objects.filter(username=request.user.username).first()
        content_per_page= 15
        p = paginator.Paginator(posts, content_per_page)
        try:
            post_page = p.page(page)
        except paginator.EmptyPage:
            post_page = paginator.Page([], page, p)
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            context = {
            'posts': post_page,
            'panding_qty':panding_qty,
            'profile':profile,
            }
            return render(request,'dashboard/mts_dashboard.html', context)
        else:
            content = ''
            for item in post_page:
                content += render_to_string('dashboard/mts_dashboard_item.html', {'item': item}, request=request)
            return JsonResponse({
                "content": content,
                "end_pagination": True if page >= p.num_pages else False,
                })

    if request.method=='POST':
    	json=[]
    	pk =  request.POST['test_id']
    	Test_Data.objects.filter(pk=pk).update(checked_by=request.user, checked_date=datetime.now())
    	posts = Test_Data.objects.filter(checked_by__isnull=True).order_by('-id')
    	for x in posts:
    		json.append({'id':x.id,
    			'tested_meter_no':x.tested_meter_no,
    			'reading_as_found':x.reading_as_found,
				'book':x.book,
				'account':x.account,
				'comments':x.comments,
				'date':x.created_date})

    	return JsonResponse(json, safe=False)



@login_required
@role_required(['admin', 'AGM'])		#For user Group test
def agm_dashboard(request):
    if request.method=="GET":
        page = int(request.GET.get('page', 1))
        posts = Test_Data.objects.filter(office =request.user.office, counter_sign_by__isnull=True, checked_by__isnull=False)
        panding_qty = Test_Data.objects.filter(office =request.user.office, counter_sign_by__isnull=True, checked_by__isnull=False).count()
        profile= CustomUser.objects.filter(username=request.user.username).first()
        content_per_page= 15
        p = paginator.Paginator(posts, content_per_page)
        try:
            post_page = p.page(page)
        except paginator.EmptyPage:
            post_page = paginator.Page([], page, p)
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            context = {
            'posts': post_page,
            'panding_qty':panding_qty,
            'profile':profile,
            }
            return render(request,'dashboard/agm_dashboard.html', context)
        else:
            content = ''
            for item in post_page:
                content += render_to_string('dashboard/agm_dashboard_item.html', {'item': item}, request=request)
            return JsonResponse({
                "content": content,
                "end_pagination": True if page >= p.num_pages else False,
                })

    if request.method=='POST':
    	json=[]
    	agm_id= request.user.username
    	pk =  request.POST['test_id']
    	Test_Data.objects.filter(pk=pk).update(agm=agm_id, agm_date=datetime.now())
    	posts = Test_Data.objects.filter(mts__isnull=False ,agm__isnull=True).order_by('-id')
    	for x in posts:
    		json.append({'id':x.id,
    			'tested_meter_no':x.tested_meter_no,
    			'reading_as_found':x.reading_as_found,
				'book':x.book,
				'account':x.account,
				'comments':x.comments,
				'date':x.date})

    	return JsonResponse(json, safe=False)



@login_required
@role_required(['admin', 'BS']) 			#For user Group test
def bs_dashboard(request):
    if request.method=="GET":
        page = int(request.GET.get('page', 1))
        posts = Test_Data.objects.filter(office =request.user.office, bs__isnull=True, agm__isnull=False, mts__isnull=False)
        panding_qty = Test_Data.objects.filter(office =request.user.office, bs__isnull=True, agm__isnull=False, mts__isnull=False).count()
        profile= CustomUser.objects.filter(username=request.user.username).first()
        content_per_page= 15
        p = paginator.Paginator(posts, content_per_page)
        try:
            post_page = p.page(page)
        except paginator.EmptyPage:
            post_page = paginator.Page([], page, p)
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            context = {
            'posts': post_page,
            'panding_qty':panding_qty,
            'profile':profile,
            }
            return render(request,'dashboard/bs_dashboard.html', context)
        else:
            content = ''
            for item in post_page:
                content += render_to_string('dashboard/bs_dashboard_item.html', {'item': item}, request=request)
            return JsonResponse({
                "content": content,
                "end_pagination": True if page >= p.num_pages else False,
                })

    if request.method=='POST':
    	json=[]
    	bs_id= request.user.username
    	pk =  request.POST['test_id']
    	#Test_Data.objects.filter(pk=pk).update(bs=bs_id, bs_date=datetime.now())
    	posts = Test_Data.objects.filter(bs__isnull=True).order_by('-id')
    	for x in posts:
    		json.append({'id':x.id,
    			'tested_meter_no':x.tested_meter_no,
    			'reading_as_found':x.reading_as_found,
				'book':x.book,
				'account':x.account,
				'comments':x.comments,
				'date':x.date})

    	return JsonResponse(json, safe=False)
