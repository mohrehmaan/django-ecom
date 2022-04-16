from django.shortcuts import render

def ex(request):
    return render(request , 'ex.html')


def Master(request):
    return render(request , 'master.html')

def Index(request):
    return render(request , 'index.html')

def Shop(request):
    return render(request , 'shop.html')

def Review(request):
    return render(request , 'review.html')

def About(request):
    return render(request , 'about.html')

def Blog(request):
    return render(request , 'blog.html')

def Contact(request):
    return render(request , 'contact.html')