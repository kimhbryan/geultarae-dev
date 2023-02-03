from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

from .models import Writing


@login_required
def index(request):
    start_date = timezone.make_aware(datetime(2023, 2, 2, 17, 00, 00))
    days = (timezone.now() - start_date).days
    context = {
        'id_1': (2 * days) + 1,
        'id_2': (2 * days) + 2
    }
    return render(request, 'index.html', context=context)


@login_required
def ask(request):
    return render(request, 'ask.html')


@login_required
def mypage(request):
    return render(request, 'mypage.html')


@login_required
def writing(request, pk):
    w = get_object_or_404(Writing, pk=pk)
    current_user = request.user
    if not w.is_available:
        return HttpResponseRedirect(reverse('index'))
    if (pk % 2 == 0) and (str(pk - 1) in current_user.writings):
        return HttpResponseRedirect(reverse('index'))
    if (pk % 2 == 1) and (str(pk + 1) in current_user.writings):
        return HttpResponseRedirect(reverse('index'))

    context = {
        'writing': w,
    }

    if str(pk) not in current_user.writings:
        current_user.writings += str(pk)
        current_user.save()
    return render(request, 'writing.html', context=context)
