from modeltranslation.translator import translator, TranslationOptions

from .models import *


class DescTranslater(TranslationOptions):
    fields = ('desc',)


class VideoTranslater(TranslationOptions):
    fields = ('video_desc',)


translator.register(Desc, DescTranslater)
translator.register(Video, VideoTranslater)
