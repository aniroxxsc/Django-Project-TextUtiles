# I have created this file

from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#    return HttpResponse ('''<h1>hello Anirudh Bhai</h1> <a href = "https://www.facebook.com"> Django code with Anirudh </a>''')
#def about(request):
#    return HttpResponse ("about anirudh bhai")
 
 
def index(request):
    return render (request, 'index.html')
    
def analyze(request):
    #Get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charactercounter = request.GET.get('charactercounter','off')

    print(removepunc)
    print(djtext)
    Punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
    analyzed=""
    if removepunc == "on":
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
    #Analyze the text
        return render(request,'analyze.html',params)
    
    elif (fullcaps == "on"):
        analyzed = djtext.upper()
        params={'purpose':'Change to Upper Case', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif (newlineremover == "on"):
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params={'purpose' : 'Removed new line', 'analyzed_text' : analyzed}
        return render(request,'analyze.html',params)
    elif (extraspaceremover == "on"):
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params={'purpose' : 'Extra Space Remover', 'analyzed_text' : analyzed}
        return render(request,'analyze.html',params)
    elif (charactercounter == "on"):
        count=0
        for index,char in enumerate(djtext):
            if char != " " and char not in Punctuations:
                count+=1
        analyzed = count
        params = {'purpose' : 'Character Count','analyzed_text' : analyzed}
        return render(request,'analyze.html',params)

    #Analyze the text
    else:
        return HttpResponse(djtext)
    
#def capfirst(request):
#    return HttpResponse("capialize first")
    
#def newlineremove(request):
#    return HttpResponse("newlineremover")
    
#def spaceremove(request):
#    return HttpResponse("space remover <a href='/'> back</a>")
    
#def charcount(request):
#    return HttpResponse("charcount")


