from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def ask(request):
    return render(request, 'ask.html')


@login_required
def mypage(request):
    return render(request, 'mypage.html')

# TO CHANGE TO GENERIC WRITING VIEW
@login_required
def writing1(request):
    return render(request, 'writing1.html')


@login_required
def writing2(request):
    return render(request, 'writing2.html')
