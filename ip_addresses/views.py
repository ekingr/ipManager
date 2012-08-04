# Create your views here.

from ip_addresses.models import *
from django.http import HttpResponse

def display(request, address=None):
    if not address:
        msg = 'Top of the address tree'
    else:
        msg = 'Top level address: %s' % address
    return HttpResponse(msg)