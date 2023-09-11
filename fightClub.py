import random

class Karakter:
    def __init__(self, adi, saglik, saldiri_gucu):
        self.adi = adi
        self.saglik = saglik
        self.saldiri_gucu = saldiri_gucu

    def saldir(self, dusman):
        vurus_gucu = random.randint(0, self.saldiri_gucu)
        dusman.saglik -= vurus_gucu
        print(f"{self.adi} {dusman.adi}'a {vurus_gucu} hasar verdi.")

    def hayatta_mi(self):
        return self.saglik > 0

def oyun():
    oyuncu = Karakter("Oyuncu", 100, 50)
    dusman = Karakter("Düşman", 100, 40)

    while oyuncu.hayatta_mi() and dusman.hayatta_mi():
        print(f"{oyuncu.adi} Sağlık: {oyuncu.saglik}, {dusman.adi} Sağlık: {dusman.saglik}")
        print("1. Vur")
        print("2. Kaç")
        secim = input("Seçiminizi yapın (1/2): ")

        if secim == "1":
            oyuncu.saldir(dusman)
            if dusman.hayatta_mi():
                dusman.saldir(oyuncu)
        elif secim == "2":
            dusman.saldir(oyuncu)
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen 1 veya 2 girin.")

    if oyuncu.hayatta_mi():
        print("Tebrikler, düşmanı yendiniz!")
    else:
        print("Üzgünüm, oyunu kaybettiniz.")

if __name__ == "__main__":
    oyun()
