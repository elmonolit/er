from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict = {'boldmessage': "hihihihih"}
    return render(request,"testapp/index.html", context = context_dict)
def testapp(request):
    return HttpResponse("hi,there")

# Create your views here.
