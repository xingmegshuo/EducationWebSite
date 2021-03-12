from django.db import models

from django.utils.translation import gettext_lazy as _
from django.conf import settings
import hashlib


# Create your models here.


class User(models.Model):
    phone = models.CharField(max_length=20, help_text=_("手机号"), verbose_name=_("手机号"))
    password = models.CharField(max_length=15, help_text=_("密码"), verbose_name=_("密码"))
    name = models.CharField(max_length=20, help_text=_("用户名"), verbose_name=_("用户名"))
    identity = models.BooleanField(verbose_name=_('用户身份'), help_text=_("用户身份"), default=False)

    class Meta:
        verbose_name = _("用户管理")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    video = models.FileField(verbose_name=_("视频"), help_text=_("视频"), upload_to="video")
    video_pic = models.ImageField(verbose_name=_("视频封面"), help_text=_("视频封面"), upload_to='pic')
    video_desc = models.TextField(verbose_name=_("视频介绍"), help_text=_("视频介绍"))
    is_show = models.BooleanField(verbose_name=_("是否展示"), help_text=_("是否展示"), default=True)

    class Meta:
        verbose_name = _("视频管理")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.video_desc


class Desc(models.Model):
    pic = models.ImageField(verbose_name=_("图片"), help_text=_("图片"), upload_to='pic')
    desc = models.TextField(verbose_name=_("图片介绍"), help_text=_("图片介绍"))
    is_show = models.BooleanField(verbose_name=_("是否展示"), help_text=_("是否展示"), default=True)

    class Meta:
        verbose_name = _("展示介绍")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.desc


class Live(models.Model):
    push_url = models.CharField(max_length=1000, verbose_name=_("推流地址"), help_text=_("推流地址"))
    pull_url = models.CharField(max_length=1000, verbose_name=_("拉流地址"), help_text=_("拉流地址"))
    push_img = models.ImageField(verbose_name=_("推流二维码"), help_text=_("推流二维码"), upload_to='pic')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("主播"), help_text=_("主播"))

    class Meta:
        verbose_name = _("直播配置")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name