class komputer:
    karta = "NVIDIA"
    procesor = "INTEL"
    stan = ""

    def wymien(self):
        self.procesor = "AMD"
        print("Wymiana procesora | Wymiana na ", self.procesor)

    def wylacz(self):
        self.stan = "OFF"
        print("Wylaczanie | ", self.stan)

    def wlacz(self):
        self.stan = "ON"
        print("Wlaczanie | ", self.stan)


obiekt = komputer()

print("Karta: ", obiekt.procesor)
print("Procesor: ", obiekt.karta, "\n")

obiekt.wlacz()
obiekt.wymien()
obiekt.wylacz()
