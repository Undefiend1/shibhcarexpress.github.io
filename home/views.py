from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Advertise, Request
from .forms import RequestFrom
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
def homepage(request):
    advertise = {
        "adds":Advertise.objects.last()
    }
    return render(request,"home/home.html",advertise)

def request(request):
    submitted = False
    if request.method == "POST":
        form = RequestFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("request?submitted=True")
    else:
        form = RequestFrom
        if "submitted" in request.GET:
            submitted = True
        return render(request, "home/request.html",{"form":form, "submitted":submitted})

def request_list(request):
    requests = {
    "data":Request.objects.all()
}
    return render(request,"home/requestlist.html",requests)

def delete_request(request,id):
    person = Request.objects.get(pk=id)
    person.delete()
    return redirect('request_list')
    
def logoutuser(request):
    logout(request)
    messages.success(request,("You have logged out Successfully"))
    return redirect('home')