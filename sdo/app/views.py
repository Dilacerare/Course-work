from django.shortcuts import render
from .models import Users, Students, Cycles, Groups


def users_list(request):
    users = Users.objects.all()
    return render(request, 'app/users.html', context={'ur_list': users})


def cycles_list(request):
    cycles = Cycles.objects.all()
    return render(request, 'app/cycles.html', context={'cyc_list': cycles})


def groups_list(request):
    groups = Groups.objects.all()
    return render(request, 'app/groups.html', context={'gr_list': groups})
