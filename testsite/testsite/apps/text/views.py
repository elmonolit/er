from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")
def test(request):
    return HttpResponse("test")

# Create your views here.
