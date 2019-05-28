from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.http import HttpResponse
# from app01.myform import User as FUser
# from app01.models import User
from app01.models import Essay,Patent,Expert
from django.contrib import messages
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.

def essayView(request):
    paper_id = request.GET['paper_id']
    result = Essay.objects.filter(paper_id=paper_id)
    if not result.exists():
        messages.success(request, "目标页面不存在！")
        return render(request, 'app01/viewachieve.html')
    else:
        result=result[0]
        paper={}
        paper['name']=result.paper_name
        paper['author']=result.author_name
        paper['summary']=result.summary
        paper['institute']=result.institute
        return render(request, 'app01/viewachieve.html',paper)

def expertView(request):
    expert_id = request.GET['expert_id']
    result = Expert.objects.filter(expert_id=expert_id)

    if not result.exists():
        messages.success(request, "目标不存在！")
        return HttpResponseRedirect('expert/')
    else:
        return HttpResponse("<h1>"+result[0].name+"</h1><h2>"+result[0].position+"</h2><h3>"+result[0].institute+"</h3><h4>"+result[0].direction+"</h3><h4>"+result[0].contact+"</h4><p>"+result[0].introduction+"</p>")

def patentView(request):
    patent_id = request.GET['paper_id']
    result = Patent.objects.filter(patent_id=patent_id)

    if not result.exists():
        messages.success(request, "目标不存在！")
        return HttpResponseRedirect('patent/')
    else:
        return HttpResponse("<h1>"+result[0].patent_name+"</h1><h2>"+result[0].author_name+"</h2><h3>"+result[0].institute+"</h3><p>"+result[0].introduction+"</p>")

