#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:19:57 2021

@author: honepa
"""

from getpass import getpass
from mysql.connector import connect, Error

hst = 'localhost'
usr = 'root'
passwd = getpass("passwd: ")

try:
    with connect(
            host = hst,
            user = usr,
            password =  passwd,
            )  as connection:
        with connection.cursor() as cursor:
            print(connection)
except Error as e:
    print(e)


    