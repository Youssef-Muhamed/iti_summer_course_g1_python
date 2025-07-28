from django.shortcuts import render

# Create your views here.
def index(request):
    users = ['anton','osama','amnna','alaa','khalifa','jehad','carol','ahmed']
    return render(request, 'contactus/index.html',context={'users':users})