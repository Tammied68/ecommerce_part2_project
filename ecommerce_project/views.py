from django.shortcuts import render

def home(request):
    """
    Landing page view for the application.
    """
    return render(request, "home.html")