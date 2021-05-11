from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def index(request):
    # return HttpResponse("hello Django")
    return render(request, "index.html")


def login(request):
    if request.method.upper() == 'POST':
        username = request.get('username','')
        password = request.get('password','')
        print(f'用户名：{username},密码：${password}')
    return HttpResponse('login success!')
