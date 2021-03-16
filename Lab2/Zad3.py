"""
Created on Tue Mar  16 9:40:34 2021
@author: piotr
"""

"""
    Zadanie 3
"""

liczby = [14, 8, 36, 44, 88, 95, 16, 63, 42, 49, 45, 39, 6, 23, 7, 52, 46, 75, 30, 2, 29, 86, 37, 100, 87, 2, 35, 21]

enum = enumerate(liczby)

for x in enum:
    print(x)

print ("\nWartość min: ", min(liczby))
print("Indeks: ", liczby.index(min(liczby)))

print ("\nWartosc max: ", max(liczby))
print ("Indeks: ", liczby.index(max(liczby)))
