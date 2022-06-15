from django.shortcuts import render
from django.http import HttpResponse

from .tasks import add

def ExampleView(request):
	add.delay(5, 19)
	return HttpResponse("OK")