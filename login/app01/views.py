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
    user = request.session.get('user',False)

    return render(request,'app01/index.html',{'user':user})


# 显示页面
def registerView(request):
    user = request.session.get('user', False)
    print(user)
    if not user:
        return render(request, 'app01/login.html')
    else:
        return HttpResponseRedirect('/index/')


def userinfoView(request,user_id):
    user = request.session.get('user', False)
    try:
        result = Account.objects.get(user_id=user_id)
    except:
        messages.success(request, "异常错误，返回首页")
        return HttpResponseRedirect('/index/')
    print(user)
    return render(request, 'app01/userinfo.html', {'data': result})


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

    try:
        result = Account.objects.get(user_name=user, password=password)  # filter
    except:
        result = None

    if result is None:
        messages.success(request, "用户名或密码不正确！")
        return HttpResponseRedirect('/registerView/')
    else:
        request.session['user'] = result.user_id #修改了
        return HttpResponseRedirect('/index/')


# 注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')


# def search(request):
#      str = request.POST.get('search_string')
#      return HttpResponseRedirect('https://www.baidu.com', str)
