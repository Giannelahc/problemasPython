# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:26:31 2020

@author: Giannela HC
"""

import numpy as np

while True:
    numero = input("Ingrese número: ")
    if len(numero)>0 and len(numero)<6:
        arreglo = [int(num) for num in numero]
        n = np.array(arreglo)
        print("Suma: {}".format(n.sum()))
        break
    pass

