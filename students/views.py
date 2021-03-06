# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/piv.png'},
        {'id': 3,
         'first_name': u'Подоба',
         'last_name': u'Віталій',
         'ticket': 2123,
         'image': 'img/podoba3.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Add Student</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'Група 1',
         'leader_id': 1,
         'leader_name': u'Віталій Подоба'},
        {'id': 2,
         'name': u'Група 2',
         'leader_id': 2,
         'leader_name': u'Корост Андрій'},
        {'id': 3,
         'name': u'Група 3',
         'leader_id': 3,
         'leader_name': u'Віталій Подоба'},
        {'id': 4,
         'name': u'Група 4',
         'leader_id': 1,
         'leader_name': u'Віталій Подоба'},
        {'id': 5,
         'name': u'Група 5',
         'leader_id': 2,
         'leader_name': u'Корост Андрій'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
