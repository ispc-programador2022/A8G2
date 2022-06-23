# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:13:36 2022

@author: Juan Manuel
"""
#El programa calcula la media de los valores flotantes almacenados en la lista
#num_rand. La media es almacenada en la variable med_num_rand
import random
import statistics

num_rand = []
med_num_rand = []

def genrnd(a, b):
    for i in range(50):
        num_rand.append(random.uniform(a,b))
      
def media(c):
    med_num_rand = statistics.mean(c)
    return med_num_rand
        
genrnd(100, 200)

print(num_rand)

print(media(num_rand))
