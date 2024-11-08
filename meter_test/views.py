from django.shortcuts import render
from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render(request,'404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html')
    response.status_code = 500
    return response

def handler400(request, *args, **argv):
    response = render(request, '400.html')
    response.status_code = 400
    return response



def custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)
