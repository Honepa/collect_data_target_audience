#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:32:17 2021

@author: honepa
"""

from getpass import getpass
from mysql.connector import connect, Error

select = "select koor_x, koor_y from interes_and_points"

file = open("bad_koor.py", 'w')
file.write("bad = [ ")

try:
    with connect(
            host = '109.68.212.119',
            user = input("us_name: "),
            password =  getpass("passwd: "),
            database = "collect_interes_vk_api",
            )  as connection:
        with connection.cursor() as cursor:
            cursor.execute(select)
            for row in cursor.fetchall():
                data = "[" + str(row[1]) + ", " + str(row[0]) + "], " 
                file.write(data + '\n')
except Error as e:
    print(e)

file.write("]")
file.close()