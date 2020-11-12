from django.shortcuts import render
from mysite.forms import UserForm

# Create your views here.
def splash(request):
    return render(request, "splash.html")

def register(request):
    user = UserForm()
    return render(request, "register.html", {'form':user})

