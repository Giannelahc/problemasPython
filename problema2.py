# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:29:07 2020

@author: Giannela HC
"""
import numpy as np

#arreglo = np.random.randint(10,size=5)
#arreglo2 = np.random.randint(10,size=5)

lista = []
lista2 = []
for n in range(6):
    lista.append(int(input("ingrese numero para arreglo 1: ")))

for n in range(6):
    lista2.append(int(input("ingrese numero para arreglo 2: ")))

print(lista)
print(lista2)

print(np.array(lista).min() in lista2)