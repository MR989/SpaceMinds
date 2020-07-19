from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')


def blogpost(request):
    return render(request,'blogpost.html')





    