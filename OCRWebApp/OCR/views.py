from django.shortcuts import render

# import pytesseract to convert text in image to string
import pytesseract

# import summarize to summarize the ocred text
#from gensim.summarization.summarizer import summarize

from .forms import ImageUpload
import os

# import Image from PIL to read image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from django.conf import settings

from googletrans import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio
import IPython.display as ipd
from .forms import NameForm
from django.http import HttpResponseRedirect

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
# Create your views here.
def index(request):
    text_en = ""
    det_text = ""
    message = ""
    #audiotts = ""
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
                #img = ImageOps.grayscale(im)
                translator = Translator()
                xyz = 'en'
                reader = easyocr.Reader([xyz])
                translator = Translator()
                bounds = reader.readtext(img, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-')
                text_list = reader.readtext(img, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-', detail=0)
                text_comb=' '.join(text_list)
                det_text = text_comb
                draw_boxes(img, bounds)
                img.show()
                
                #text = text_comb
                text_trans = translator.translate(text_comb)
                text_en = text_trans.text
                #audiotts = ipd.Audio('trans.mp3')
                #audio=gTTS(text_en.text)
                #audio.save('trans.mp3')
                #text = pytesseract.image_to_string(im)
                #text_en = pytesseract.image_to_string(im, lang=xyz)
                #text_en = translator.detect(text)
                #from langdetect import detect_langs 
                #text_en = detect_langs(sample_text)
                #text_en = text_en.encode("ascii", "ignore")
                #text_en = text_en.decode()
                os.remove(pathz)
            except:
                message = "check your filename and ensure it doesn't have any space or check if it has any text"

    context = {
        'det_text': det_text,
        'translated_text': text_en,
        'message': message
    }
    return render(request, 'formpage.html', context)
