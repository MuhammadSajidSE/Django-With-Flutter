from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def hello(request):
    return HttpResponse("Hello, world!")
