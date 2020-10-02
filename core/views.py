from django.shortcuts import render,redirect
from .models import RegModel
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def home(request):
    context = {}
    data = RegModel.objects.all()
    context['data']=data
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        state = request.POST['state']
        zips = request.POST['zip']
        

        form = RegModel(email=email,password=password,city=city,state=state,zips=zips)
        if form:
            form.save()
            context['msg']="data succesfully saved"
            context['cls']="alert-success"
        else:
            
            context['msg']="Sorry Something is worng"
            context['cls']="alert-danger"



        print(email,password,city,state,zip)
    return render(request,"core/index.html",context)

def update(request):
    context = {}
    rid = request.GET['uid']
    data = RegModel.objects.get(id=rid)
    context['data']=data
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        state = request.POST['state']
        zips = request.POST['zip']
        data.email=email
        data.password =password
        data.city=city
        data.state=state
        data.zips=zips
        if data:
            data.save()
            context['msg']="data succesfully saved"
            context['cls']="alert-success"
        else:
            
            context['msg']="Sorry Something is worng"
            context['cls']="alert-danger"

    return render(request,'core/edit.html',context)

def delete(request):
    rid = request.GET['uid']
    pi = RegModel.objects.get(id=rid)
    pi.delete()
    return HttpResponseRedirect('/')