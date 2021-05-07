""" Kalkulator """

## START PROGRAMU ##

print("#------------------------------------------------------#")
print("|                   Kalkulator RPN                     |")
print("#------------------------------------------------------#")
print("| Dostępne operacje:                                   |")
print("|    (+) Dodawanie                                     |")
print("|    (-) Odejmowanie                                   |")
print("|    (*) Mnozenie                                      |")
print("|    (/) Dzielenie                                     |")
print("|                                                      |")
print("|   Kalkulator działa na odwrotniej notacji polskiej   |")
print("#------------------------------------------------------#")

#-------------------------------#
#       Klasa Kalkulator        #
#===============================#

class Kalkulator:

    # inicjalizacja
    def __init__(self):
        self.wynik = 0

    # dodawanie
    def dodawanie(self, a, b):
        self.wynik = a + b

    # odejmowanie
    def odejmowanie(self, b, a):
        self.wynik = a - b

    # mnozenie
    def mnozenie(self, a, b):
        self.wynik = a * b

    # dzielenie
    def dzielenie(self, a, b):
        self.wynik = a / b

kalk = Kalkulator()

# Pobieranie danych wejsciowych
print("\nPodaj wyrazenie do obliczenia: ")
wejscie = input(" |#| ")

# Zapisanie danych do tablicy
znaki = wejscie.split(" ")
# Okreslenie ilosci danych
liczba_znakow = len(znaki)
# Tablica pomocnicza
tab = []

# Sprawdzanie poprawnosci
# print(znaki)
# print(liczba_znakow)

# Przejscie tablicy z zapisanymi danymi wejsciowymi
for ilosc in range(liczba_znakow):
    #print("ilosc")
    if znaki[ilosc] != '+' and znaki[ilosc] != '-' and znaki[ilosc] != '*'  and znaki[ilosc] != '/':
        tab.append(znaki[ilosc])
    else:
        # jezeli istnieja dane
        if bool(tab) == True:
            # przypisz liczbe a
            a = int(tab.pop())
        else:
            break

        # jezeli istnieja dane
        if bool(tab) == True:
            # przypisz liczbe b
            b = int(tab.pop())
        else:
            break

        # Obsluga operacji
        if znaki[ilosc] == '+':
            kalk.dodawanie(a, b)
        if znaki[ilosc] == '-':
            kalk.odejmowanie(a, b)
        if znaki[ilosc] == '*':
            kalk.mnozenie(a, b)
        if znaki[ilosc] == '/':
            kalk.dzielenie(a, b)

        # Zapisywanie wyniku operacji
        if znaki[ilosc] == '+' or znaki[ilosc] == '-' or znaki[ilosc] == '*' or znaki[ilosc] == '/':
            tab.append(kalk.wynik)

if bool(tab) == True:
     if len(tab) != 1:
        print("\n |!!!| Blad - za malo dzialan |!!!| ")
     else:
        print("\n |☻| Wynik: ", tab[0])
else:
    print("\n |!!!| Blad - za malo liczb |!!!|")
