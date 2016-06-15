# -*- coding: UTF-8 -*-

import requests


def sembed():
	r = requests.get('http://api.randomuser.me/?results='+str(3))
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
	return resultlist

print(sembed())
