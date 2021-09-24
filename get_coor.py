#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:06:40 2021

@author: honepa
"""

"""
rq = requests.get('https://nominatim.openstreetmap.org/search?format=json&q=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&polygon_geojson=1')
coor = rq.json()
json_ob = json.dumps(coor)
with open("json/first_coor.json", "w") as outfile:
    outfile.write(json_ob)
print(json_ob)
"""

"""
from bs4 import BeautifulSoup

svg = open("json/Moscow_all_districts.svg").read()

soup = BeautifulSoup(svg, 'xml')
paths = soup('path')[-1]
print(paths['d'])

"""

from coor_administrative import coordinates

def point_in_poly(p, poly):
    x, y = p
    odd = False
    
    for segment_a, segment_b in zip(poly, poly[1:] + [poly[0]]):
        x_a, y_a = segment_a
        x_b, y_b = segment_b
        if (y_a < y <= y_b) or (y_b < y <= y_a):
            if (x_a + (y - y_a) / (y_b - y_a) * (x_b - x_a)) < x:
                odd = not odd
    
    return odd


min_x = coordinates[0][0][0][0]
min_y = coordinates[0][0][0][1]
max_x = 0.0
max_y = 0.0

#j = 0
file = open("moscow_koor.py", 'w')
file.write("msk_koor = [ ")
#file_cr = open("x_y", 'w')
for i in range(len(coordinates)):
    for j in range(len(coordinates[i][0])):
        #data = str(coordinates[i][0][j][0]) + " " + str(coordinates[i][0][j][1])
        #file.write(data + '\n')
        if coordinates[i][0][j][0] < min_x:
            min_x = coordinates[i][0][j][0]
        if coordinates[i][0][j][0] > max_x:
            max_x = coordinates[i][0][j][0]
        if coordinates[i][0][j][1] < min_y:
            min_y = coordinates[i][0][j][1]
        if coordinates[i][0][j][1] > max_y:
            max_y = coordinates[i][0][j][1]

x, y = min_x, min_y
d_x = (max_x - min_x) / (75*2)
d_y = (max_y - min_y) / (98*2)
counter = 0

print(str(x) + " " + str(y))

while max_x >= x:
    x += d_x
    while max_y >= y:
        y += d_y
        for i in range(len(coordinates)):
            if point_in_poly([x, y], coordinates[i][0]):
                counter += 1
                data = "[" + str(x) + ", " + str(y) + "], " 
                file.write(data + '\n')
    y = min_y
file.write("]")
print(str(x) + " " + str(y))
print(counter)

file.close()
