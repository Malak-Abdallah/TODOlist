from django.shortcuts import render



def intro(request):
    return render(request, 'index/index.html')

