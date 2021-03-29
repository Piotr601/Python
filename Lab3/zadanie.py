"""
    Zadanie 3
Systemy wbudowane
"""

import re

naglowek="""    From : author@example.com
    User-Agent : Thunderbird 1.5.0.9 (X11/20061227)
    MIME-Version : 1.0
    To : editor@example.com """

nadawca, ua, wersja, odbiorca = naglowek.split('\n')

slownik = {
    'From': nadawca,
    'User-Agent': ua,
    'MIME-Version': wersja,
    'To': odbiorca,
}

for y in slownik:
    print(slownik[y])

""" Uzycie wyrazen regularnych """

# Adres mail - wyrażenie regularne
adres_mail= r'[\w\.\_\-]+@[\w\.\_\−]+'

# Nadawca
szukaj_nadawcy = re.search(adres_mail, nadawca)
if szukaj_nadawcy:
    print("\nNadawca:  ", szukaj_nadawcy.group())

# User-Agent
ua_f = ua.split(r':',1)
print("U−A:     ", ua_f[1])

# Wersja
wersja_f = wersja.split(r': ',1)
print("Wersja:   ", wersja_f[1])

# Odbiorca
szukaj_odbiorcy = re.search(adres_mail, odbiorca)
if szukaj_odbiorcy:
    print("Odbiorca: ", szukaj_odbiorcy.group())


