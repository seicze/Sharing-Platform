from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.http import HttpResponse
# from app01.myform import User as FUser
# from app01.models import User
from app01.models import Essay,Patent,Expert,HotSpot
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
        str = result.keywords
        str = str.split(";", str.count(';'))
        for i in str:
            if i == '':
                continue
            res = HotSpot.objects.filter(keyword=i)
            if not res.exists():
                add = HotSpot(keyword=i, num=1)
                add.save()
            else:
                res = res[0]
                num = res.num + 1
                HotSpot.objects.filter(keyword=i).update(num=num)

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
    patent_id = request.GET['paper_id']
    result = Patent.objects.filter(patent_id=patent_id)

    if not result.exists():
        messages.success(request, "目标不存在！")
        return HttpResponseRedirect('patent/')
    else:
        return HttpResponse("<h1>"+result[0].patent_name+"</h1><h2>"+result[0].author_name+"</h2><h3>"+result[0].institute+"</h3><p>"+result[0].introduction+"</p>")

def hotspot(request):
    essay = Essay.objects.all()
    for paper in essay:
        str = paper.keywords
        str = str.split(";", str.count(';'))
        for i in str:
            if i == '':
                continue

            res = HotSpot.objects.filter(keyword=i)
            if not res.exists():
                add = HotSpot(keyword = i, num = 1)
                add.save()
            else:
                res = res[0]
                num = res.num + 1
                HotSpot.objects.filter(keyword = i).update(num=num)
    return HttpResponse("game over!")
