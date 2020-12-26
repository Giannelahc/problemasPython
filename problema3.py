# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:55:16 2020

@author: Giannela HC
"""
import numpy as np

arreglo = np.random.randint(100,size=100)

lista = list(arreglo)
arr = []


def eliminar(lista,n):
    for i in lista:
        if i == n :
            lista.remove(i)

for n in lista:
    if lista.count(n)>=2:
        arr.append(n)
        eliminar(lista,n)
        
print(arreglo)
print(arr)