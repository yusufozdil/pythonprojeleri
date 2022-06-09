sayi1= float(input("İlk Sayınızı Giriniz: "))
sayi2= float(input("İkinci Sayınızı Giriniz: "))

islem= int(input("İşlem Numaranızı Giriniz: 1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme: "))

if (islem == 1):
    print(sayi1+sayi2)
elif islem == 2:
    print(sayi1-sayi2)
elif islem == 3:
    print(sayi1*sayi2)
elif islem == 4:
    print(sayi1/sayi2)
else:
    print("Lütfen Belirtilen Numaralardan Birini Giriniz")