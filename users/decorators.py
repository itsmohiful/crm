from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func


def user_permission(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print('group name= ',group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            if group == 'customer':
                return HttpResponse("you are not able to view this page ! ")
                #return redirect('/customer_page')

        return wrapper_func
    return decorator
