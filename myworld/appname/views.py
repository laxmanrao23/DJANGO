from django.shortcuts import render
from django.http import HttpResponse
from .forms import MemberForm
from .models import Member

# Create your views here.


def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'homepage.html')


def register(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {'a': 'Saved Successfully'}
        return render(request, 'aregistration.html', context)
    else:
        return render(request, 'aregistration.html', {})


def blank(request):
    all_members = Member.objects.all
    context = {'all' : all_members}
    return render(request, 'blankpage.html', context)
