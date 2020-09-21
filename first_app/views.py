# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render
from first_app.models import data
from . import forms
from django.http import HttpResponse, HttpResponseRedirect

def get_key():
    k = data.objects.all()
    all_key = [str(i.key) for i in k]
    key = ''
    for i in range(4):
        a = random.randrange(97,122)
        key = key + chr(a)
    if key in all_key:
        return get_key()
    else:
        return key
def index(request):
    a = data()
    form1 = forms.text()
    if request.method == 'POST': # If the form has been submitted...
            form1 = forms.text(request.POST) # A form bound to the POST data
            if form1.is_valid(): # All validation rules pass
                z =  form1.cleaned_data['text']
                keys = get_key()
                a.key = keys
                a.text = z
                a.save()
                url_re = "http://127.0.0.1:8000/"+keys
                return HttpResponseRedirect(url_re)
    dic = {'form':form1}

    return render(request, "pastebin.html", context = dic )
# Create your views here.
def redirect1(request, genre):
    x = data.objects.all()
    l = [str(i.key) for i in x]
    if genre not in l:
        return HttpResponse("<center><h1>404 URL NOT FOUND</h1</center>")
    else:
        b = data.objects.get(key=genre)
        show = str(b.text)
        link = "http://127.0.0.1:8000/"+genre
        link = str(link)
        dic = {'data' : show, 'link' : link}
        return render(request, "pastebinshow.html", context = dic )


