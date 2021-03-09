"""
Created on Tue Mar  9 10:03:55 2021

@author: piotr

Program wyznaczajacy pierwiastki trojmianu
"""

import math

while True:
    a = float(input('a='))
    b = float(input('b='))
    c = float(input('c='))
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-1*b + math.sqrt(delta ))/(2*a)
        x2 = (-1*b - math.sqrt(delta ))/(2*a)
        print('Dwa pierwiastki',x1 ,',',x2)
    elif delta == 0:
        x = -1*b /(2*a)
        print('Jeden pierwiastek',x)
    else:
        print('Program nie osbluguje liczb zepolonych')

    print('Czy chcesz kontynuowac prace? T/N')
    decyzja=input()

    if decyzja=='N':
        print('Koniec programu')
        break
