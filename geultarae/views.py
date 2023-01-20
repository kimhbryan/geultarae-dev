from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Writing


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def ask(request):
    return render(request, 'ask.html')


@login_required
def mypage(request):
    return render(request, 'mypage.html')


@login_required
def writing(request, pk):
    w = get_object_or_404(Writing, pk=pk)
    context = {
        'writing': w,
    }
    return render(request, 'writing.html', context=context)
