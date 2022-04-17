
from django.shortcuts import render
from ec.models import Category

def ex(request):
    return render(request , 'ex.html')


def Master(request):
    return render(request , 'master.html')

def Index(request):
    category = Category.objects.all()

    context = {
        'category': category,
    }
    return render(request , 'index.html', context)

def Shop(request):
    category = Category.objects.all()

    context = {
        'category': category,
    }
    return render(request , 'shop.html',context)

def Review(request):
    return render(request , 'review.html')

def About(request):
    return render(request , 'about.html')

def Blog(request):
    return render(request , 'blog.html')

def Contact(request):
    return render(request , 'contact.html')