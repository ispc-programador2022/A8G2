# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:57:27 2022

@author: Juan Manuel
"""

#El programa calcula la mediana de los valores flotantes almacenados en la lista
#num_rand. La media es almacenada en la variable mediana_num_rand
import random
import statistics

num_rand = []
med_num_rand = []
mediana_num_rand =[]
var_num_rand=[]

def genrnd(a, b):
    for i in range(50):
        num_rand.append(random.uniform(a,b))
      
def media(c):
    med_num_rand = statistics.mean(c)
    return med_num_rand

def mediana(d):
    mediana_num_rand = statistics.median(d)
    return mediana_num_rand

def rango(e):
    rango_num_rand = len(e)
    return rango_num_rand

def varianza(f):
    var_num_rand = statistics.variance(f)
    return var_num_rand
        
genrnd(100, 200)

print(num_rand)

print(media(num_rand))

print(mediana(num_rand))

print(rango(num_rand))

print(varianza(num_rand))