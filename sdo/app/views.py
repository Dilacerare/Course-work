from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Users, Students, Cycles, Groups
from .forms import groupForm, cycleForm


def users_list(request):
    users = Users.objects.all()
    return render(request, 'app/users.html', context={'ur_list': users})


def cycles_list(request):
    cycles = Cycles.objects.all()
    return render(request, 'app/cycles.html', context={'cyc_list': cycles})


def groups_list(request):
    groups = Groups.objects.all()
    return render(request, 'app/groups.html', context={'gr_list': groups})


def groups_add(request):
    if request.method == 'POST':
        form = groupForm(request.POST)
        if form.is_valid():
            Groups.objects.create(**form.cleaned_data)
            return redirect('groups_list')
    else:
        form = groupForm()
        return render(request, 'app/addgroup.html', {'form': form})


def cycles_add(request):
    if request.method == 'POST':
        form = cycleForm(request.POST)
        if form.is_valid():
            Cycles.objects.create(**form.cleaned_data)
            return redirect('cycles_list')
    else:
        form = cycleForm()
        return render(request, 'app/addcycle.html', {'form': form})


def cycles_delete(request, id):
    try:
        cycle = Cycles.objects.get(id=id)
        cycle.delete()
        return redirect('cycles_list')
    except Cycles.DoesNotExist:
        return HttpResponseNotFound("<h2>Цикл не найден</h2>")


def groups_delete(request, id):
    try:
        group = Groups.objects.get(id=id)
        group.delete()
        return redirect('groups_list')
    except Groups.DoesNotExist:
        return HttpResponseNotFound("<h2>Группа не найден</h2>")
