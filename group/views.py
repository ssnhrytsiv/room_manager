import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from group.forms import GroupForm
from .models import Group
# Create your views here.

def groups(request):
    groups = Group.get_all()
    context = {
        'groups': groups
    }
    return render(request, 'group/group.html', context)

def create(request):
    if request.method == "POST":
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        group = Group(name=data['name'],description=data['description'])
        group.save()
        return redirect('/group')
    else:
        return render(request, 'group/create.html')

def edit(request, pk):
    post = Group.get(pk)
    context = {
            'post': post
        }
    return render(request, 'group/edit.html', context)


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Group.delete_by_id(data['id']):
            return HttpResponse(status=200, )
    return HttpResponse(status=400)


def show(request, pk):
    group = Group.get(pk=pk)
    # users = User.objects.filter(group=group)
    context = {
        'group': group,
        # 'users': users
    }
    return render(request, 'group/show_group.html', context)