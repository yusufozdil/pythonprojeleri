import random
secenek=["taş","kağıt","makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
print("Taş,Kağıt, Makas oyununa hoşgeldinizn Oyunu bitirmek için q tuşuna basın")
while True:
    secim = input("taş mı, kağıt mı, makas mı? ")
    bil_secim = random.choice(secenek)
    if secim==taş:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş, Sonuç: Berabere")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt, Kaybettiniz")
        else:
            print("Bilgisayarın seçimi: Makas, Sonuç:Kazandınız")
    if secim==kağıt:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş, Sonuç: Kazandınız")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt, Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: Makas, Sonuç:Kaybettiniz")
    if secim==makas:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş, Sonuç: Kaybettiniz")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt, Sonuç: Kazandınız")
        else:
            print("Bilgisayarın seçimi: Makas, Sonuç:Berabere")
    if secim=='q':
        print("Çıkılıyor...")
        break