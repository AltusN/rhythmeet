from django.shortcuts import render, HttpResponse

# Create your views here.
def view_all_gymnasts(request):
    return HttpResponse('this is a response from all')