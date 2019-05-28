from django.shortcuts import render_to_response, render
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def logout(request, *args, **kwargs):
    from django.contrib.auth.views import logout
    from django.shortcuts import HttpResponseRedirect
    logout(request, *args, **kwargs)
    return HttpResponseRedirect(request.build_absolute_uri('/index'))
