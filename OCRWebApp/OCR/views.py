from django.shortcuts import render

from .forms import ImageUpload
import os
import shutil
# import Image from PIL to read image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from django.conf import settings
from .forms import Lang
from django.http import HttpResponseRedirect
from googletrans import Translator
import easyocr
from gtts import gTTS

from IPython.display import Audio
import IPython.display as ipd
import cv2

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def get_lang(request):
    lang = request.POST.get('lang')
    return lang

# Create your views here.
def index(request):
    text_en = ""
    det_text = ""
    message = ""
    lang = get_lang(request)
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                image = request.FILES['image']
                image = image.name
                path = settings.MEDIA_ROOT
                pathz = path + "/images/" + image
                img = Image.open(pathz)
                translator = Translator()
                xyz = lang
                reader = easyocr.Reader([xyz])
                translator = Translator()
                bounds = reader.readtext(img, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-')
                text_list = reader.readtext(img, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-', detail=0)
                text_comb=' '.join(text_list)
                det_text = text_comb
                draw_boxes(img, bounds)
                img.show()
                text_trans = translator.translate(text_comb)
                text_en = text_trans.text
                audio=gTTS(text_en)
                audio.save('trans.wav')
                shutil.move("trans.wav", "C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/Sem 5 Study Material/Mini Project/OCRWebApp/static/audio/trans.wav")
                os.remove(pathz)
            except:
                message = "check your filename and ensure it doesn't have any space or check if it has any text"

    context = {
        'det_text': det_text,
        'translated_text': text_en,
        'message': message
    }
    return render(request, 'formpage.html', context)
