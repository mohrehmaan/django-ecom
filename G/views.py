from django.shortcuts import render

def ex(request):
    return render(request , 'ex.html')


def Master(request):
    return render(request , 'master.html')

def Index(request):
    return render(request , 'index.html')