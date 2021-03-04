from django.urls import path, re_path
from .views import home_view, login, video, mobile_home,mobile_video

urlpatterns = [
    path('', home_view),
    path('index.m',mobile_home),
    path('login', login),
    re_path(r'^(\d+)/$', video),
    re_path(r'^m(\d+)/$',mobile_video),
]
