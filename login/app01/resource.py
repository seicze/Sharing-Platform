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
        return HttpResponseRedirect('/index/')
    else:
        result = result[0]

        click = Essay.objects.get(paper_id=paper_id)
        click.clicks = result.clicks + 1
        click.save()

        paper={}
        paper['name']=result.paper_name
        paper['author']=result.author_name
        paper['introduction'] = result.introduction
        paper['institute']=result.institute
        paper['source'] = result.source
        paper['keywords'] = result.keywords
        paper['clicks'] = result.clicks
        paper['db'] = result.db
        paper['cssci'] = result.cssci
        paper['download_link'] = result.download_link
        paper['published_time'] = result.published_time
        paper['user_id'] = request.session.get('user_id',False)
        return render(request, 'app01/viewEssay.html', paper)

def expertView(request):
    expert_id = request.GET['expert_id']
    result = Expert.objects.filter(expert_id=expert_id)

    if not result.exists():
        messages.success(request, "目标不存在！")
        return HttpResponseRedirect('expert/')
    else:
        return HttpResponse("<h1>"+result[0].name+"</h1><h2>"+result[0].position+"</h2><h3>"+result[0].institute+"</h3><h4>"+result[0].direction+"</h3><h4>"+result[0].contact+"</h4><p>"+result[0].introduction+"</p>")

def patentView(request):
    patent_id = request.GET['patent_id']
    result = Patent.objects.filter(patent_id=patent_id)

    if not result.exists():
        return HttpResponseRedirect('/index/')
    else:
        result = result[0]

        click = Patent.objects.get(patent_id=patent_id)
        click.clicks = result.clicks + 1
        click.save()

        patent={}
        patent['name']=result.patent_name
        patent['author']=result.author_name
        patent['introduction'] = result.introduction
        patent['clicks'] = result.clicks
        patent['app_number']=result.app_num
        patent['app_date']=result.app_date
        patent['publish_number'] = result.public_number
        patent['published_time'] = result.published_time
        patent['source'] = result.source
        patent['appliant'] = result.appliant
        patent['address'] = result.address
        patent['agency'] = result.agency
        patent['agent'] = result.agent
        patent['main_cls_num']=result.main_cls_num
        patent['patent_cls_num']=result.patent_cls_num
        patent['code']=result.code
        patent['page']=result.page
        #patent['download_link'] = result.download_link
        patent['user_id'] = request.session.get('user_id',False)
        return render(request, 'app01/viewPatent.html', patent)

