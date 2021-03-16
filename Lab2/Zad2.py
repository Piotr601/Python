"""
Created on Tue Mar  16 9:40:34 2021
@author: piotr
"""

"""
    Zadanie 2
"""

plik = open('zdanie.txt','r').read()
print('Tekst z pliku:\n\n', plik, '\n')

litera = {}
suma_liter=0

for x in plik:
    x = x.upper()
    if x != ' ' and x != '\n':
        suma_liter += 1
        if x in litera:
            litera[x] += 1
        else:
            litera[x] = 1

for y in litera:
    print('Litera:',y,' Ilosc:' , litera[y])

print('\nDlugosc zdania (ze spacjami)', len(plik))
print('Dlugosc zdania (bez spacji)', suma_liter)