from django.contrib import admin
from .models import *


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


class DescAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class LiveUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Desc, DescAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Live, LiveUserAdmin)
