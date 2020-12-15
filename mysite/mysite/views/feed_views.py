from django.shortcuts import render

# Create your views here.
def gratitude_feed(request):
    return render(request, "home.html")
