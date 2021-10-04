from django.contrib import admin

# Register your models here.
from .models import Ocr
admin.site.register(Ocr)

from .models import AudioFile
admin.site.register(AudioFile)
