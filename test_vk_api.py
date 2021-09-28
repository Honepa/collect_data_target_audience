#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:35:40 2021

@author: honepa
"""
#import vk_api
import json
import requests
from user_agent import generate_user_agent
from interes_categories import interes2
from getpass import getpass
from time import sleep, time

#session = vk_api.VkApi(token = "")

#vk = session.get_api() 
"""
criter = {
        "interest_categories" : 'Культурный отдых, афиша, мероприятия',
        "geo_near" : '72.9579,95.2403,500'}
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36"}
json_geo = json.dumps(criter)

rq = requests.post("https://api.vk.com/method/ads.getTargetingStats?account_id=&access_token=&v=5.131&link_url=https://vk.com/dev/ads.getTargetingStats&link_domain=vk.com&criteria=" + json_geo, headers = { 'User_Agent' : generate_user_agent()})
print(json.loads(rq.text)['response']['audience_count'])
"""
#print(vk.ads.getTargetingStats(account_id = ,  v = '5.131', access_token = '', link_url =  "https://vk.com/dev/ads.getTargetingStats", link_domain = "vk.com", criteria = json_geo))
start_time = time()
acc_id = getpass("account_id: ")
acc_token = getpass("access_token: ")

for i in range(len(interes2)):
    criter = {
        "interest_categories" : interes2[i],
        "geo_near" : '55.711762566837045,37.959665523333335,500'}
    json_geo = json.dumps(criter)
    rq = requests.post("https://api.vk.com/method/ads.getTargetingStats?account_id=" + str(acc_id) + "&access_token=" + str(acc_token) + "&v=5.131&link_url=https://vk.com/dev/ads.getTargetingStats&link_domain=vk.com&criteria=" + json_geo, headers = { 'User_Agent' : generate_user_agent()})
    #print(str(interes2[i]) + " " + str(json.loads(rq.text)['response']['audience_count']))
    print(rq.text)
    del criter, json_geo, rq
    sleep(2)
print(time() - start_time)