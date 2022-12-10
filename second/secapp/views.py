from django.shortcuts import render
from django.http import HttpResponse
from .models import Member2
from .forms import MemberForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {'a': 'saved successfully'}
        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html', {})


def course_details(request):
    return render(request, 'course_details.html')


def courses(request):
    return render(request, 'courses.html')


def events(request):
    return render(request, 'events.html')


def pricing(request):
    return render(request, 'pricing.html')


def trainers(request):
    return render(request, 'trainers.html')
