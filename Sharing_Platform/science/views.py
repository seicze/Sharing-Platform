from django.shortcuts import render,HttpResponseRedirect
from science.models import *
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    keyword=request.GET['keyword']
    result=Essay.objects.filter(Q(paper_name__contains=keyword)|Q(author_name__contains=keyword)|Q(institute__contains=keyword)|Q(summary__contains=keyword))
    return render(request,"searchresult.html",{'result':result})