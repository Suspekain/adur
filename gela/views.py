from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import random

def gela(request):
    return render(request, 'gela/gela.html')

def txanponak_bota(request):
    txanponak = []
    for x in range(5):
        txanponak.append(random.choice([True, False]))
    print(txanponak)

    conext = {
        "txanponak" : txanponak
    }

    return render(request, 'gela/gela.html', txanponak)
    #return HttpResponse("""<html><script>window.location.replace('/g');</script></html>""")
