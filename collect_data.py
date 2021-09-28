#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:26:08 2021

@author: honepa
"""
import json
import requests
from getpass import getpass
from time import sleep
from user_agent import generate_user_agent
from interes_categories import interes2
from mysql.connector import connect, Error
from moscow_koor import msk_koor

def collect_data_from_vk_api(acc_id, acc_token, usr, passwd, db_name, interes, koor, lnk_url, lnk_domain, second):
    error = 0
    try:
        criter = {
        "interest_categories" : interes,
        "geo_near" : f"{koor[1]},{koor[0]},500"}
        json_geo = json.dumps(criter)
        rq = requests.post(f"https://api.vk.com/method/ads.getTargetingStats?account_id={acc_id}&access_token={acc_token}&v=5.131&link_url={lnk_url}&link_domain={lnk_domain}&criteria=" + json_geo, headers = { 'User_Agent' : generate_user_agent()})
        audit =  str(json.loads(rq.text)['response']['audience_count'])
        data = f"insert into interes_and_points (koor_x, koor_y, link, category_name, count_person) values ({koor[1]}, {koor[0]}, '{lnk_url}', '{interes}', {audit})"
        try:
            with connect(
                    host = 'localhost',
                    user = usr,
                    password = passwd,
                    database = db_name,
                    ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(data)
                    connection.commit()
                    #print(data)
        except Error as e:
            print(e)
            error += 1
        del criter, json_geo, rq
        sleep(second)
    except LookupError:
        print(rq.text)
        error += 1
    return error

if __name__ == '__main__':
    lnk_url = "https://vk.com/dev/ads.getTargetingStats"
    lnk_domain = "vk.com"
    
    print("vk api data:")
    acc_id = getpass("account_id: ")
    acc_token = getpass("access_token: ")
    
    print("Mysql data:")
    usr = input("user name: ")
    passwd = getpass("passwd: ")
    db_name = "collect_interes_vk_api"
    
    interes = interes2[0]
    errors = 0
    
    for i in range(len(msk_koor)):
        koor = msk_koor[i]
        errors += collect_data_from_vk_api(acc_id, acc_token, usr, passwd, db_name, interes, koor, lnk_url, lnk_domain, 2)
        if errors >= 10:
            pass
        print('count = %d error_count = %d'%(i, errors))
    print(errors)