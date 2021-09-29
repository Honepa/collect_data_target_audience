#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:46:55 2021

@author: honepa
"""

from bad_koor import bad
from moscow_koor import msk_koor
from koor import koor
#import numpy as np
"""
file = open("koor.py", 'w')
file.write("koor = [ ")



for i in range(len(nf_list)):
    data = "[" + str(nf_list[0]) + ", " + str(nf_list[1]) + "], " 
    file.write(data + '\n')
file.write("]")    
file.close()
"""
nf_list = [item for item in msk_koor if item not in bad]

for i in range(len(nf_list)):
    print(msk_koor.index(nf_list[i]))