from django.core.management.base import BaseCommand, CommandError
from shortener.models import Link
from django.contrib.auth.models import User
import requests


class Command(BaseCommand):
    help = 'test'

    def add_arguments(self, parser):
        parser.add_argument('fakenumber', nargs='+', type=int)

    def handle(self, *args, **options):
        adres = 'http://api.randomuser.me/?results='+str(options['fakenumber'][0])
        r = requests.get(adres)
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
        User.objects.all().delete()
        for item in resultlist:
            user = User.objects.create_user(username=item['username'],
            first_name=item['first_name'],
            last_name=item['last_name'],
            email=item['email'],
            password=item['password'])
            user.save()
