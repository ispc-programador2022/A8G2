# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 00:05:50 2022

@author: Juan Manuel
"""

#La función genrnd genera una lista de 500.000.000.000.000.000 números flotantes 
#entre los argumentos a (límite inferior) y b (límite superior). Dicha lista se
#llama num_rand


import random
num_rand = []

def genrnd(a, b):
    for i in range(500000000000000000):
        num_rand.append(random.uniform(a,b))
        
        
genrnd(100, 200)
print(num_rand)