import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Entries


def entries(request):
    e = Entries.objects.filter(user=request.user.id)
    print(request.user.id)
    print(e.values())
    return render(request, 'entries.html', {'entries': e})


def delete(request, id):
    e = Entries.objects.filter(id=id).delete()
    return redirect('/')
    

def read(request, id):
    if id >= 1:
        e = Entries.objects.filter(id=id).first()
        return render(request, 'read.html', {'entry': e})


def entry(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if request.user.id is None:
            userid = 'anonymous'
        else:
            userid = request.user.id

        e = Entries.objects.create(
            title=body['title'],
            user=userid,
            entry=body['content'],
        )
        e.save()
        return HttpResponse("success")

    return render(request, 'entry.html')