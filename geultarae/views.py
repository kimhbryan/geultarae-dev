from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

from .models import Writing


@login_required
def index(request):
    start_date = timezone.make_aware(datetime(2023, 2, 3, 17, 00, 00))
    days = (timezone.now() - start_date).days
    context = {
        'id_1': (3 * days) + 1,
        'id_2': (3 * days) + 2,
        'id_3': (3 * days) + 3
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

    def already_chosen(id, chosen):
        remaining = [i for i in range(1, 4) if i != id]
        for elm in remaining:
            if str(((id - 1) // 3) + elm) in chosen:
                return True
        return False

    if (not w.is_available) or (already_chosen(pk, current_user.writings)):
        return HttpResponseRedirect(reverse('index'))

    context = {
        'writing': w,
    }

    if str(pk) not in current_user.writings:
        current_user.writings += str(pk)
        current_user.save()

    return render(request, 'writing.html', context=context)
