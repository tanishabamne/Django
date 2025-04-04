from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    x="<h1> hello world </h1>"
    return HttpResponse(x)
def about (request):
    data={'name':True,'age':False,'quals':None}
    return JsonResponse(data)
def index(request):
    return render(request,'index.html')
def new(request):
    return redirect('https://www.google.com')


def index(request):
    x={}
    data=[{'name':'tanisha','city':'bhopal'}]
    x['key1']=data
    return render(request,'index.html',x)

