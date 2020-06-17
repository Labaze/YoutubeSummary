import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests as req
import re
from gensim.summarization import summarize


def index(request):
    return render(request, 'home/index.html')


@csrf_exempt
def results(request):
    # context = summarize_gensim(request)
    context = {}
    if request.method == "POST":
        youtube_url = request.POST.get('url')
        language = request.POST.get('language')
        slider_value = float(request.POST.get('slider'))
    end_url = re.findall('v=.*', youtube_url)
    print(youtube_url)
    print(language)
    youtube_caption_url = f'http://video.google.com/timedtext?lang={language}&{end_url[0]}'
    reponse = req.get(youtube_caption_url)
    print("ici")
    if reponse.text == "":
        return HttpResponse(json.dumps({"resume": "It's complicated to create a summary since the video does not have subtitles."}, ensure_ascii=False).encode('utf8'),
                            content_type="application/json")
    soup = BeautifulSoup(reponse.content, 'html.parser')  # the parser that suits to the html
    text = soup.text.replace("\n", " ").replace("&quot", "").replace(".", ". ").replace("&#39;", "\'").replace("…",
                                                                                                               ". ").replace(
        "–", ". ").replace("?", "? ").replace("\r\n", ". ")
    context['resume'] = summarize(text, ratio=slider_value)
    print(context['resume'])

    # return render(request, 'home/results.html',context)
    return HttpResponse(json.dumps({"resume": "%s" % context['resume']}, ensure_ascii=False).encode('utf8'),
                        content_type="application/json")

	# return JsonResponse({"resume": "%s" % context['resume']}, status=200)
