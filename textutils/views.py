
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("Everything about yourself")

 
def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    toxi = request.POST.get('removepunc','off')
    uppercase = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline','off')
    extraspace = request.POST.get('extraspace','off')
    charcount = request.POST.get('charcount','off')

    if (toxi == "on"):
    
        punctuations = ''' « »,()[]{}⟨ ⟩"",'';: '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose': 'remove punctutions', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(uppercase == 'on'):
            analyzed = ''
            for char in djtext:
                 analyzed = analyzed + char.upper()
            
            param = {'purpose': 'Convert into uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
    
    if(newline=='on'):
        analyzed = ''
        for char in djtext:
                if char != '\n' and char!="\r":
                   analyzed = analyzed + char
        
        param = {'purpose': 'Newline', 'analyzed_text': analyzed}
        djtext = analyzed
         
    if(extraspace == 'on'):
        analyzed = ''
        for index,char in enumerate(djtext):
                if not djtext[index] == " ":
                   analyzed = analyzed + char
        
        param = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
         
    if(charcount == 'on'):
        analyzed = len(djtext)
        
        param = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
         
    if(toxi != 'on' and uppercase!='on' and newline!='on' and extraspace!='on' and charcount!='on'):
        return HttpResponse('Error')
    
    return render(request,'analyze.html',param)