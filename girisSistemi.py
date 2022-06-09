f = open("isimler.txt", "r")
whatthereturn ="None"




soru=input("Kayıtlı Bir Kullanıcı Mısınız?(y/n): ")
if soru=="y":

        isim=input("İsminiz Nedir? ")
        if isim in f.read():
            whatthereturn=isim
            print("Hoşgeldiniz! ")
        else:
            print("Kayıtlı Kullanıcı Bulunamadı. ")

elif soru=="n":
        kayıtSoru=input("Kayıt Olmak İster Misiniz?(y/n): ")
        
        if kayıtSoru=="y":
            isim=input("İsminiz Nedir? ")

            if isim in f.read():
                print("Zaten Kayıtlı Bir Kullanıcısınız. ")
                f.close()

            else:
                a=open("isimler.txt", "a")
                a.write(isim)
                a.close()   
                print("Hoşgeldiniz! ")

        elif kayıtSoru=="n":
            print("Sağ Yukarıdaki Çarpıya Bas Cınım ")

        else:
            print("Lütfen Geçerli Bir Cevap Girin")

else:
        print("Progrramı Tekrar Çalıştır ve Ne Yazdığımı Oku. ")




