from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video.urls')),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
]
