#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:00:30 2021

@author: honepa
"""

from getpass import getpass
from mysql.connector import connect, Error

create_bd = "CREATE DATABASE collect_interes_vk_api";
create_table = """
    CREATE TABLE interes_and_points(
        id INT AUTO_INCREMENT PRIMARY KEY,
        koor_x REAL,
        koor_y REAL,
        category_name VARCHAR(255),
        link VARCHAR(500),
        count_person BIGINT UNSIGNED
)
"""

#insert_data = "insert into interes_and_points (koor_x, koor_y, category_name, count_person) values (37.959665523333335, 55.71624751224521, 'Ноутбуки, компьютеры и комплектующие', 5156556165)"


try:
    with connect(
            host = 'localhost',
            user = input("us_name: "),
            password =  getpass("passwd: "),
            )  as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_bd)
            connection.commit()
    try:
        with connect(
                host = 'localhost',
                user = input("us_name: "),
                password =  getpass("passwd: "),
                database = "collect_interes_vk_api",
                )  as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_table)
                connection.commit()
    except Error as e:
        print(e)
except Error as e:
    print(e)

"""
try:
    with connect(
            host = 'localhost',
            user = input("us_name: "),
            password =  getpass("passwd: "),
            database = "collect_interes_vk_api",
            )  as connection:
        with connection.cursor() as cursor:
            cursor.execute(insert_data)
            connection.commit()
except Error as e:
    print(e)

"""