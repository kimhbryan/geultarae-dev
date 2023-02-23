from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .forms import AskForm
from .models import Writing


@login_required
def index(request):
    start_date = timezone.make_aware(datetime(2023, 2, 17, 17, 00, 00))
    days = (timezone.now() - start_date).days
    base_id = 3 * days
    context = {
        f"writing{i-base_id}":
        Writing.objects.get(pk=i) for i in range(base_id + 1, base_id + 4)
    }
    return render(request, 'index.html', context=context)


@login_required
def ask(request):
    return render(request, 'ask.html')


@login_required
def mypage(request):
    cur_user = request.user

    chosen = cur_user.writings.strip().split()
    idxs = {((int(i) - 1) // 3) + 1: i for i in chosen}

    datas = {}

    for i in range(1, 15):
        if i in idxs.keys():
            w = get_object_or_404(Writing, pk=idxs[i])
            title = w.title
            date = f"{w.date_available.month}/{w.date_available.day}"
            datas[i] = {
                "title": title,
                "date": date,
                "link": f"/writing/{idxs[i]}"
            }
        else:
            datas[i] = {
                "title": "선택하지 않음",
                "date": "1/1",
                "link": "#"
            }

    return render(request, 'mypage.html', {'datas': datas})


@login_required
def writing(request, pk):
    w = get_object_or_404(Writing, pk=pk)
    current_user = request.user

    chosen_list = current_user.writings.strip().split()

    def cannot_choose(id, chosen):
        remainder = id % 3 + (3 if id % 3 == 0 else 0)
        remaining = [i for i in range(1, 4) if i != remainder]
        for elm in remaining:
            if str(((id - 1) // 3) * 3 + elm) in chosen:
                return True
        return False

    def already_chosen(id, chosen):
        return str(id) in chosen

    if (not w.is_available and not already_chosen(pk, chosen_list)) or (cannot_choose(pk, chosen_list)):
        return HttpResponseRedirect(reverse('index'))

    if not already_chosen(pk, current_user.writings):
        current_user.writings += str(pk) + " "
        current_user.save()

    return render(request, 'writing.html', context={'writing': w})


@login_required
def plot(request, pk):
    w = get_object_or_404(Writing, pk=pk)
    current_user = request.user

    chosen_list = current_user.writings.strip().split()

    def already_chosen(id, chosen):
        return str(id) in chosen

    if not already_chosen(pk, chosen_list):
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

    form = AskForm()
    return render(request, 'ask.html', {'form': form})


@login_required
def ask_done(request):
    return render(request, 'ask_done.html')
