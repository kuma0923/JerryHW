from django.shortcuts import render
from .models import *

# Create your views here.

def mother(request):
	content = ''
	if request.method == 'POST':
		content = request.POST.get('content')
		Mother.objects.create(content=content)
	return render(request, 'mothers_day.html', {'content': content})