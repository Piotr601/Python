"""
Created on Tue Mar  16 9:40:34 2021
@author: piotr
"""

"""
    Zadanie 1
"""
zdanie = "Witaj, tu twój program"
litera = {}
suma_liter=0

for x in zdanie:
    x = x.upper()
    if x != ' ':
        suma_liter += 1
        if x in litera:
            litera[x] += 1
        else:
            litera[x] = 1

for y in litera:
    print('Litera:',y,' Ilosc:' , litera[y])

print('Dlugosc zdania (ze spacjami)', len(zdanie))
print('Dlugosc zdania (bez spacji)', suma_liter)
