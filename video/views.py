from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse
import hashlib


# Create your views here.

# 首页
def home_view(request):
    desc = Desc.objects.all()
    video = Video.objects.all()
    if 'name' in request.COOKIES:
        name = request.COOKIES['name']
        return render(request, 'video/home.html', {"name": name, "desc": desc, "video": video})
    else:
        return render(request, 'video/home.html', {"desc": desc, "video": video})


def mobile_home(request):
    desc = Desc.objects.all()
    video = Video.objects.all()
    if 'name' in request.COOKIES:
        name = request.COOKIES['name']
        return render(request, 'mobile/home.html', {"name": name, "desc": desc, "video": video})
    else:
        return render(request, 'mobile/home.html', {"desc": desc, "video": video})


# 登录
def login(request):
    # md5 = hashlib.md5()
    account = request.POST.get('account')
    password = request.POST.get('password')
    try:
        user = User.objects.get(phone=account, password=password)
        response = JsonResponse({"status": 'ok', "name": user.name})
        response.set_cookie('name', user.name, max_age=1800)
        return response
    except:
        return JsonResponse({'status': 'error', "name": "登录失败"})


# 视频
def video(request, id):
    v = Video.objects.get(id=id)
    if 'name' in request.COOKIES:
        name = request.COOKIES['name']
        return render(request, 'video/palyVido.html', {'video': v, 'name': name})
    else:
        return render(request, 'video/palyVido.html', {'video': v})


def mobile_video(request, id):
    v = Video.objects.get(id=id)
    if 'name' in request.COOKIES:
        name = request.COOKIES['name']
        return render(request, 'mobile/palyVido.html', {'video': v, 'name': name})
    else:
        return render(request, 'mobile/palyVido.html', {'video': v})


# 直播
def live_video(request):
    return render(request, 'video/zhibo.html')
