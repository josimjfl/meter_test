from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

def role_required(allowed_roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)

            #check ajax api request or not. if api true
            elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
                print("ooooooooooooo")
                data = {"status":"failed", "message":"দুঃখিত, এই পরিবর্তনটি করতে আপনি অনুমতি প্রাপ্ত নন।"}
                return JsonResponse(data, safe=False)

            #if html page request
            else:
            	raise PermissionDenied
        return _wrapped_view
    return decorator