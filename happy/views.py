from django.shortcuts import render
from .models import *

# Create your views here.


def DisplayHappyNamesToHomePage(request):
    happy = HappyWasabi.objects.all()

    context = {
        "happy": happy,
    }

    return render(request, "Happypage.html", context)
