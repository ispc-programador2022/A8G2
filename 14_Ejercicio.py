# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:57:55 2022

@author: Juan Manuel
"""

#La función genrnd genera una lista de 50 números flotantes 
#entre los argumentos a (límite inferior) y b (límite superior). Dicha lista se
#llama num_rand

from itertools import combinations
import random
import math

num_rand = []

def genrnd(a, b):
    for i in range(50):
        num_rand.append(random.uniform(a,b))
        
def comb_prod(c):
    temp = combinations(c, 2)
    for i in list(temp):
        print(math.prod(i))
        
genrnd(100, 200)
print(num_rand)

comb_prod(num_rand)