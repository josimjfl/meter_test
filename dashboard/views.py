from django.shortcuts import render
from test_data.models import Test_Data
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import User
from django.core import paginator
from django.http import JsonResponse
from datetime import datetime




@login_required
def user_dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    return render(request, "dashboard/user_dashboard.html", {'profile':profile, 'role': role})


@login_required
@role_required(['admin'])
def admin_dashboard(request):
    profile = CustomUser.objects.all().order_by('-id')
    return render(request, "dashboard/admin_dashboard.html", {'profile':profile})


@login_required
@role_required(['admin', 'IT'])          #For user Group test    
def it_dashboard(request):
    profile = CustomUser.objects.all().order_by('-id')
    return render(request, "dashboard/it_dashboard.html", {'profile':profile})


@login_required
@role_required(['admin', 'MT', 'MTS']) 			#For user Group test	
def mt_dashboard(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))  # Get the requested page number or default to 1

        # Filter the queryset
        posts = Test_Data.objects.filter(
            office=request.user.office,
            checked_by__isnull=True
        ).order_by('-id')

        pending_qty = posts.count()

        # Pagination setup
        content_per_page = 10
        paginator_obj = Paginator(posts, content_per_page)
        
        try:
            post_page = paginator_obj.page(page)
        except EmptyPage:
            post_page = paginator_obj.page(paginator_obj.num_pages)  # Return the last page if out of range

        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Serialize data for JSON response
            serialized_data = [
                {
                    "id": obj.id,
                    "meter_no": obj.tested_meter_no,
                    "reading": obj.reading_as_found,
                    "book": obj.book,
                    "account": obj.account,
                    "result": obj.comments,
                    "print_counter": obj.print_counter,
                    "date": obj.created_date.strftime('%Y-%m-%d') if obj.created_date else None,
                }
                for obj in post_page
            ]

            return JsonResponse({
                "content": serialized_data,
                "total_pages": paginator_obj.num_pages,
            })

        # Render the full page for non-AJAX requests
        context = {
            "posts": post_page,
            "pending_qty": pending_qty
        }
        return render(request, 'dashboard/mt_dashboard.html', context)

    elif request.method == "POST":
        # Handle updates for received_by field
        test_id = request.POST.get('test_id')
        if test_id:
            posts = Test_Data.objects.filter(pk=test_id).update(
                checked_by=request.user, 
                checked_date=datetime.now(),
            )

        data = { "id": test_id }
        return JsonResponse(data, safe=False)





@login_required
@role_required(['admin', 'MTS', 'MT']) 			#For user Group test
def mts_dashboard(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))  # Get the requested page number or default to 1

        # Filter the queryset
        posts = Test_Data.objects.filter(
            office=request.user.office,
            checked_by__isnull=True
        ).order_by('-id')

        pending_qty = posts.count()

        # Pagination setup
        content_per_page = 10
        paginator_obj = Paginator(posts, content_per_page)
        
        try:
            post_page = paginator_obj.page(page)
        except EmptyPage:
            post_page = paginator_obj.page(paginator_obj.num_pages)  # Return the last page if out of range

        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Serialize data for JSON response
            serialized_data = [
                {
                    "id": obj.id,
                    "meter_no": obj.tested_meter_no,
                    "reading": obj.reading_as_found,
                    "book": obj.book,
                    "account": obj.account,
                    "result": obj.comments,
                    "print_counter": obj.print_counter,
                    "date": obj.created_date.strftime('%Y-%m-%d') if obj.created_date else None,
                }
                for obj in post_page
            ]

            return JsonResponse({
                "content": serialized_data,
                "total_pages": paginator_obj.num_pages,
            })

        # Render the full page for non-AJAX requests
        context = {
            "posts": post_page,
            "pending_qty": pending_qty
        }
        return render(request, 'dashboard/mts_dashboard.html', context)

    elif request.method == "POST":
        # Handle updates for received_by field
        test_id = request.POST.get('test_id')
        if test_id:
            posts = Test_Data.objects.filter(pk=test_id).update(
                checked_by=request.user, 
                checked_date=datetime.now(),
            )

        data = { "id": test_id }
        return JsonResponse(data, safe=False)





@login_required
@role_required(['admin', 'AGM', 'DGM'])		#For user Group test
def agm_dashboard(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))  # Get the requested page number or default to 1

        # Filter the queryset
        posts = Test_Data.objects.filter(
            office=request.user.office,
            checked_by__isnull=False,
            counter_sign_by__isnull = True,
        ).order_by('-id')

        pending_qty = posts.count()

        # Pagination setup
        content_per_page = 10
        paginator_obj = Paginator(posts, content_per_page)
        
        try:
            post_page = paginator_obj.page(page)
        except EmptyPage:
            post_page = paginator_obj.page(paginator_obj.num_pages)  # Return the last page if out of range

        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Serialize data for JSON response
            serialized_data = [
                {
                    "id": obj.id,
                    "meter_no": obj.tested_meter_no,
                    "reading": obj.reading_as_found,
                    "book": obj.book,
                    "account": obj.account,
                    "result": obj.comments,
                    "print_counter": obj.print_counter,
                    "date": obj.created_date.strftime('%Y-%m-%d') if obj.created_date else None,
                }
                for obj in post_page
            ]

            return JsonResponse({
                "content": serialized_data,
                "total_pages": paginator_obj.num_pages,
            })

        # Render the full page for non-AJAX requests
        context = {
            "posts": post_page,
            "pending_qty": pending_qty
        }
        return render(request, 'dashboard/agm_dashboard.html', context)

    elif request.method == "POST":
        # Handle updates for received_by field
        test_id = request.POST.get('test_id')
        if test_id:
            posts = Test_Data.objects.filter(pk=test_id).update(
                counter_sign_by=request.user, 
                counter_sign_date=datetime.now(),
            )

        data = { "id": test_id }
        return JsonResponse(data, safe=False)





@login_required
@role_required(['admin', 'BS', 'BA'])     #For user Group test
def bs_dashboard(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))  # Get the requested page number or default to 1

        # Filter the queryset
        posts = Test_Data.objects.filter(
            office=request.user.office,
            received_by__isnull=True,
            counter_sign_by__isnull=False,
            checked_by__isnull=False
        ).order_by('-id')

        pending_qty = posts.count()

        # Pagination setup
        content_per_page = 10
        paginator_obj = Paginator(posts, content_per_page)

        try:
            post_page = paginator_obj.page(page)

        except EmptyPage:
            post_page = paginator_obj.page(paginator_obj.num_pages)  # Return the last page if out of range

        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Serialize data for JSON response
            serialized_data = [
                {
                    "id": obj.id,
                    "meter_no": obj.tested_meter_no,
                    "reading": obj.reading_as_found,
                    "book": obj.book,
                    "account": obj.account,
                    "result": obj.comments,
                    "print_counter": obj.print_counter,
                    "date": obj.created_date.strftime('%Y-%m-%d') if obj.created_date else None,
                }
                for obj in post_page
            ]

            return JsonResponse({
                "content": serialized_data,
                "total_pages": paginator_obj.num_pages,
            })

        # Render the full page for non-AJAX requests
        context = {
            "posts": post_page,
            "pending_qty": pending_qty
        }
        return render(request, 'dashboard/bs_dashboard.html', context)


    elif request.method == "POST":
        # Handle updates for received_by field
        bs_id = request.user
        test_id = request.POST.get('test_id')
        if test_id:
            posts = Test_Data.objects.filter(pk=test_id).update(
                received_by=bs_id, 
                received_date=datetime.now(), 
                print_counter =+1
            )

        data = { "id": test_id }

        return JsonResponse(data, safe=False)



@login_required
@role_required(['admin', 'LT', 'LM', 'JE'])          #For user Group test    
def je_dashboard(request):
    return render(request, "dashboard/je_dashboard.html")



@login_required 
def dashboard(request):
    profile= CustomUser.objects.filter(username=request.user.username).first()
    role = profile.role if profile else None  # Get the user's role
    return render(request, "dashboard/dashboard.html", {'profile':profile, 'role': role})



def privacy_policy(request):
    return render(request, 'dashboard/privacy_policy.html')