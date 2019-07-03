from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def disconnect(request):
	return render(request, 'disconnect.html')