from django.shortcuts import render,redirect
from .models import Contact_us_model
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from myapp.forms import ImageForm
from myapp.models import Image

# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

def index2(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'e_patha/index2.html', params)

def about(request):
    return render(request, 'e_patha/about.html')

def index1(request):
    return render(request, 'e_patha/index1.html')

def indexx(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'indexx.html', {'contacts': contacts, 'search_input': search_input})

 
def Contact_us_(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact_us_m = Contact_us_model(name=name, email=email, phone=phone, desc=desc)
        Contact_us_m.save()
        thank = True
    return render(request, 'e_patha/Contact_us_.html', {'thank': thank})
     
def weather(request):
    return render(request,'e_patha/weather.html')


def home(request):
    return render(request, "e_patha/index1.html")


def gallery(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'myapp/home1.html', {'img':img, 'form':form})

def Bus_Timmings(request):
    return render(request,'e_patha/Bus_Timmings.html')
 
def map(request):
    mapbox_access_token = 'pk.eyJ1IjoiY2hpbm1heWExMjM0NTYiLCJhIjoiY2t2ZjVxbDJ2MWJsNzJ3bzhpb2p4MWI2YyJ9.dsLEZG5gifX4bH1t2-3i2Q'
    return render(request, 'e_patha/map.html', 
                  { 'mapbox_access_token': mapbox_access_token })  

def donation(request):
    return render(request,'e_patha/donation.html')

def panchayath(request):
    return render(request,'e_patha/panchayath.html')
