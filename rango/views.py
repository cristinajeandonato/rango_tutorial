from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!")

def about(request):
    return HttpResponse("This is the about page <a href='/rango/'>Index</a>")
