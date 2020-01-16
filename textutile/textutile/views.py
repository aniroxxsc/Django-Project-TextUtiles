# I have created this file

from django.http import HttpResponse
from django.shortcuts import render 
 
def index(request):
    return render (request, 'index.html')
    
def analyze(request):

    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter','off')

    Punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
    analyzed=""
    if removepunc == "on":
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
    #Analyze the text
    
    if (fullcaps == "on"):
        analyzed=""
        analyzed = djtext.upper()
        params={'purpose':'Change to Upper Case', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if (newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r" :
                analyzed = analyzed + char
        params={'purpose' : 'Removed new line', 'analyzed_text' : analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params={'purpose' : 'Extra Space Remover', 'analyzed_text' : analyzed}
        djtext = analyzed

    if (charactercounter == "on"):
        analyzed=""
        count=0
        for index,char in enumerate(djtext):
            if char != " " and char not in Punctuations:
                count+=1
        analyzed = count
        params = {'purpose' : 'Character Count','analyzed_text' : analyzed}
        djtext = analyzed

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on"):
        return HttpResponse("Error... Pls select any option")
    #Analyze the text
    return render(request,'analyze.html',params)
