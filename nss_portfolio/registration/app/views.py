from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'index.html')

def home(request):
    #  return HttpResponse('Hello World')
    return render(request,'home.html')