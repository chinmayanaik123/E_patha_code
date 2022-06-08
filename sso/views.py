from django.shortcuts import render

from django.http import HttpResponse

    
def home(request):
    return render(request, "e_patha/index1.html")
