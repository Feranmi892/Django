from django.shortcuts import render

from django.http import HttpResponse



def index(request):

    context_dict = {'boldmessage':'Learn,relearn,unlearn!!!'}
    #return HttpResponse('Hey there, welcome to rango')
    return render(request, 'rango/index.html', context =context_dict)