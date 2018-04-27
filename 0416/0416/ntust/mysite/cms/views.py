from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	students=Student.objects.all()
	return render_to_response("cms/kuma_information.html",locals())