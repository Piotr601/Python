"""
Created on Tue Mar  16 9:40:34 2021
@author: piotr
"""

"""
    Zadanie 2b
"""

litera = {}
dlugosc = 0
suma_liter = 0

with open('zdanie.txt') as plik:
    print('Tekst z pliku:\n')
    for linia in plik:
        print(linia[:-1])

        for x in linia:
            x = x.upper()
            if x != ' ' and x != '\n':
                suma_liter += 1
                if x in litera:
                    litera[x] += 1
                else:
                    litera[x] = 1

        dlugosc = dlugosc + len(linia)

    print()
    for y in litera:
        print('Litera:',y,' Ilosc:' , litera[y])

print('\nDlugosc zdania (ze spacjami)', dlugosc)
print('Dlugosc zdania (bez spacji)', suma_liter)
