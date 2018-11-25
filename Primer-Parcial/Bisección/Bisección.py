import math
import numpy as np
import matplotlib.pyplot as plt

def fun(c):
    return c**3 -7*c**2 + 14*c - 6

misvariables=[[0,1],[1,3.2],[3.2,4]]


maxIter = 100
itera = 0

for r in range (3):
    c0 = misvariables[r][0]
    c1 = misvariables[r][1]
    for i in range(maxIter):
        itera += 1
        fc0 = fun(c0)
        fc1 = fun(c1)
        if fc0 * fc1 >0:
            print("No hay raiz en este rango")
            break
        cr = (c0 + c1) / 2
        fcr = fun(cr)
        if fc0 * fcr < 0:
            c1 = cr
        else:
            c0 = cr
        if abs(fcr) < 0.00001:
            break
    print ("La raiz en el intervalo entre", misvariables[r][0], "y", misvariables[r][1], "es: %.5f"%c0)
    print ("Con %i iteraciones "%itera )
