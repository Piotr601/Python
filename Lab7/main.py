""" Kalkulator SCOKET """

import socket

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
    def dzielenie(self, b, a):
        self.wynik = a / b


def kalk_rpn(wejscie):

    # Zapisanie danych do tablicy
    znaki = wejscie.split(' ')

    # Okreslenie ilosci danych
    liczba_znakow = len(znaki)

    # Tablica pomocnicza
    tab = []

    znaki[liczba_znakow - 1] = znaki[liczba_znakow - 1][0]
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
            connection.send(b'|!!!| Blad - za malo dzialan |!!!| ')
         else:
            res = tab[0]
            connection.send(b'|:)| Wynik: ')
            connection.send(str(res).encode())
            connection.send(b'\n')
    else:
        connection.send(b' |!!!| Blad - za malo liczb |!!!|')


def menu():
    connection.send(b'#------------------------------------------------------#')
    connection.send(b'|                   Kalkulator RPN                     |')
    connection.send(b'#------------------------------------------------------#')
    connection.send(b'| Dostepne operacje:                                   |')
    connection.send(b'|    (+) Dodawanie                                     |')
    connection.send(b'|    (-) Odejmowanie                                   |')
    connection.send(b'|    (*) Mnozenie                                      |')
    connection.send(b'|    (/) Dzielenie                                     |')
    connection.send(b'|                                                      |')
    connection.send(b'|   Kalkulator dziala na odwrotniej notacji polskiej   |')
    connection.send(b'#------------------------------------------------------#')


ADDRESS = "localhost"
PORT = 23
ADR = (ADDRESS, PORT)

kalk = Kalkulator()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(ADR)
client.listen()

connection, address = client.accept()
menu()

while True:
    connection.send(b'Podaj wyrazenie: ')
    data = connection.recv(256)

    if data:
        connection.send(data)
        kalk_rpn(str(data.decode()))
    else:
        connection.close()
        connection, address = client.accept()