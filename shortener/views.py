# -*- coding: UTF-8 -*-
from django.db.models import F
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST

from shortener.baseconv import base62
from shortener.models import Link
from shortener.forms import LinkSubmitForm
import requests
from django.contrib.auth.models import User

def userview(request):
    resultlist = User.objects.all()
    context = {'resultlist': resultlist}
    return render(request, 'shortener/embeds.html',  context)


def sembed(request):
    r = requests.get('http://api.randomuser.me/?results='+str(5))
    r.encoding = "utf-8"
    json=r.json()
    dset = json["results"]
    resultlist = []
    for d in dset:
        result = {'username':None,'first_name':None,'last_name':None,'email':None,'password':None}
        result['username'] = d["login"]["username"]
        result['first_name'] = d["name"]["first"]
        result['last_name'] = d["name"]["last"]
        result['email'] = d["email"]
        result['password'] = d["login"]["password"]
        resultlist.append(result)
    return render(request, 'shortener/embeds.html', {'resultlist': resultlist})
        

@require_GET
def follow(request, base62_id):
    """
    View which gets the link for the given base62_id value
    and redirects to it.
    """
    link = get_object_or_404(Link, id=base62.to_decimal(base62_id))
    link.usage_count = F('usage_count') + 1
    link.save()
    return HttpResponsePermanentRedirect(link.url)


@require_GET
def info(request, base62_id):
    """
    View which shows information on a particular link
    """
    link = get_object_or_404(Link, id=base62.to_decimal(base62_id))
    return render(request, 'shortener/link_info.html', {'link': link})


@require_POST
def submit(request):
    """
    View for submitting a URL to be shortened
    """
    form = LinkSubmitForm(request.POST)
    if form.is_valid():
        kwargs = {'url': form.cleaned_data['url']}
        custom = form.cleaned_data['custom']
        if custom:
            # specify an explicit id corresponding to the custom url
            kwargs.update({'id': base62.to_decimal(custom)})
        print(kwargs['url'])
        if kwargs['url'] in [item.url for item in Link.objects.all()]:
            return render(request, 'shortener/submit_failed.html', {'link_form': form})
        
        link = Link.objects.create(**kwargs)
        user = User.objects.order_by('?').first()
        link.submitter = user
        link.save(update_fields=['submitter'])
        return render(request, 'shortener/submit_success.html', {'link': link})
    else:
        return render(request, 'shortener/submit_failed.html', {'link_form': form})


@require_GET
def index(request):
    """
    View for main page
    """
    values = {
        'link_form': LinkSubmitForm(),
        'recent_links': Link.objects.all().order_by('-date_submitted')[:5],
        'most_popular_links': Link.objects.all().order_by('-usage_count')[:5]}
    return render(request, 'shortener/index.html', values)


