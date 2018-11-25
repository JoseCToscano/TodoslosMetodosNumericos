# Ejemplo lagrange
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x = [1950, 1960, 1970, 1980, 1990, 2000]
y = [123.5, 131.2, 150.7, 141.3, 203.2, 240.5]


pL = ''
for k in range(len(x)):
    pL +=  str(y[k]) + '* ('
    Lxk = 1
    for j in range(len(x)):
        if (j == k):
            continue
        pL += '(x - %f)*'%(x[j])
        Lxk *= x[k] - x[j]
    pL = pL[:-1] + '/%f) +'%(Lxk) 
pL = pL[:-1]

expr = sympify(pL)
expr = expand(expr)
print(expr)

plt.plot(x,y,'ro')
x2 = np.linspace(1950,2000,200)
y2 = []
x = symbols('x')
for i in range(len(x2)):
    y2.append(expr.subs(x,x2[i]))
plt.plot(x2,y2)
