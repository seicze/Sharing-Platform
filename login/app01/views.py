from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
# from app01.myform import User as FUser
# from app01.models import User
from app01.models import Account
from django.contrib import messages
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.


class UserInfo(forms.Form):
    user_name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(error_messages={'required':u'两次密码不一致'},widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField()
    tel = forms.CharField()

    def clean(self):
        if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            self.password2 = None
        return self.cleaned_data


def index(request):
    user_id = request.session.get('user_id',False)

    return render(request,'app01/index.html',{'user_id':user_id})


# 显示页面
def registerView(request):
    user_id = request.session.get('user_id', False)
    print(user_id)
    if not user_id:
        return render(request, 'app01/login.html')
    else:
        return HttpResponseRedirect('/index/')


def userinfoView(request,user_id):
    my_user_id= request.session.get('user_id', False)
    result = Account.objects.filter(user_id=user_id)
    if not result.exists():
        messages.success(request, "异常错误，返回首页")
        return HttpResponseRedirect('/index/')
    # print(user)
    return render(request, 'app01/userinfo.html', {'data': result[0], 'user_id': my_user_id})


# 注册
def register(request):

    obj = UserInfo()
    if request.method == 'POST':
        # user_input_obj = UserInfo(request.POST)
        # if user_input_obj.is_valid():
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        tel = request.POST['tel']
        basic_info = request.POST['basic_info']
        if password1 != password2:
            messages.success(request, "密码不一致！")
            return render(request, 'app01/login.html')
        if Account.objects.filter(user_name=user_name):
            messages.success(request, "用户名重复！")
            return render(request, 'app01/login.html')
        account = Account(user_name=user_name,password=password1,email=email,tel=tel,basic_info=basic_info)
        account.save()
        check = True
        return render(request, 'app01/immediate.html',{'check':check})
        # else:
        #     error_msg = user_input_obj.errors
        #     messages.success(request, error_msg)
        #     return render(request,'app01/login.html',{'obj':user_input_obj,'errors':error_msg})
    return render(request,'app01/login.html',{'obj':obj})
    # check = False
    # if request.method == 'POST':
    #     form = app01(request.POST)
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         user = app01(**form.cleaned_data)
    #         user.save()
    #         check = True
    #         return render(request, 'app01/immediate.html',{'check':check})
    #
    # return HttpResponseRedirect('/index/')


# 登录
def login(request):

    user = request.POST['user_name']
    password = request.POST['password']

    result = Account.objects.filter(user_name=user, password=password)  # filter

    if not result.exists():
        messages.success(request, "用户名或密码不正确！")
        return HttpResponseRedirect('/registerView/')
    else:
        result = result[0]
        request.session['user_id'] = result.user_id #修改了
        request.session['user_name'] = result.user_name
        return HttpResponseRedirect('/index/')


# 注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')


# def search(request):
#      str = request.POST.get('search_string')
#      return HttpResponseRedirect('https://www.baidu.com', str)


def personal(request):
    return render(request,"app01/personal/Personal.html")

def personalmodify(request):
    return render(request,"app01/personal/PersonalModify.html")

def searchlist(request):
    return render(request,"app01/SearchList.html")
