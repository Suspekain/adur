from django.shortcuts import render
from django.http import HttpResponse
import random

def gela(request):
    return render(request, 'gela/gela.html')

def txanponak_bota(request):
    txanponak = []
    for x in range(5):
        txanponak.append(random.choice([True, False]))
    print(txanponak)

    return render(request, 'gela/gela.html')
    #return HttpResponse("""<html><script>window.location.replace('/g');</script></html>""")
