from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def allowed_users(allowed_roles=[], path='', message=''):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                messages.error(request, message)
                return redirect(path)
        return wrapper_function
    return decorator
