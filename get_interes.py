#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:45:30 2021

@author: honepa
"""

import vk_api

session = vk_api.VkApi(token = "")

vk = session.get_api() 

interes = session.method("ads.getSuggestions", {"section" : "interest_categories_v2", "country" : 1})

file = open("interes_categories.py", 'w')
file.write("interes2 = [ ")

for i in range(len(interes)):
    data = "'%s'," % interes[i]['name']
    file.write(data + '\n')
    print(interes[i]['name'])

file.write("]")
file.close()
