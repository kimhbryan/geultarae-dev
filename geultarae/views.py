from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.core.mail import BadHeaderError, send_mail
from datetime import datetime

from .models import Writing
from .forms import AskForm


@login_required
def index(request):
    start_date = timezone.make_aware(datetime(2023, 2, 6, 17, 00, 00))
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

    def cannot_choose(id, chosen):
        remaining = [i for i in range(1, 4) if i != id]
        for elm in remaining:
            if str(((id - 1) // 3) + elm) in chosen:
                return True
        return False

    def already_chosen(id, chosen):
        return str(id) in chosen

    if (not w.is_available and not already_chosen(pk, current_user.writings)) or (cannot_choose(pk, current_user.writings)):
        return HttpResponseRedirect(reverse('index'))

    if not already_chosen(pk, current_user.writings):
        current_user.writings += str(pk)
        current_user.save()

    return render(request, 'writing.html', context={'writing': w})


@login_required
def plot(request, pk):
    w = get_object_or_404(Writing, pk=pk)
    current_user = request.user

    def already_chosen(id, chosen):
        return str(id) in chosen

    if not already_chosen(pk, current_user.writings):
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'plot.html', context={'writing': w})


@login_required
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(
                    f"Inquiry from {name} ({from_email})",
                    message,
                    from_email,
                    ['skeinofwords@gmail.com']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return HttpResponseRedirect('/ask/done/')

@login_required
def ask_done(request):
    return render(request, 'ask_done.html')