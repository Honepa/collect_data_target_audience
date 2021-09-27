#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:19:57 2021

@author: honepa
"""

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
            host = 'localhost',
            user = input("us_name: "),
            password =  getpass("passwd: "),
            )  as connection:
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                print(db)
except Error as e:
    print(e)