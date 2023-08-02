# kayıt olmalı bankamatik sistemi

def kayit(hesap):
    hesapismi = input("Lütfen hesap isminizi giriniz: ")
    pin = input("lütfen PIN giriniz: ")
    baslangic_bakiye = float(input("Lütfen başlangiç bakiyenizi giriniz: "))
    hesap[hesapismi] = {"pin": pin, "bakiye": baslangic_bakiye}

def giris(hesap):
    hesapismi = input("Lütfen hesap isminizi giriniz: ")
    pin = input("Lütfen PIN giriniz: ")
    if hesapismi in hesap and hesap[hesapismi]['pin'] == pin:
        return hesapismi
    else:
        return None
    
def bakiyesorgu(hesap,hesapismi):
    print(f"Hesabinizda {hesap[hesapismi]['bakiye']} TL bulunmaktadir.")

def parayatir(hesap, hesapismi, kullanılanbakiye):
    hesap[hesapismi]['bakiye'] += kullanılanbakiye
    print(f"{kullanılanbakiye} TL hesabiniza yatirildi.Toplam Bakiye {hesap[hesapismi]['bakiye']} TL")
    
def paracekme(hesap, hesapismi, kullanılanbakiye):
    if hesap[hesapismi]['bakiye'] >= kullanılanbakiye:
        hesap[hesapismi]['bakiye'] -= kullanılanbakiye
        print(f"{kullanılanbakiye} TL para çekildi.Kalan bakiye {hesap[hesapismi]['bakiye']} TL")
    else:
        print
        ("Bakiye yetersiz!")

def anagiris():
    print("AtayBANK Hoşgeldiniz! ")

    hesap = {}

    while True:
        print("\n Yeni hesap aç [1]")
        print("\n Hesaba giriş yap [2]")
        print("\n Çikiş yap [3]")
        secim = input("Lütfen seçiminizi yapiniz (1/2/3)")
        if secim == "1":
            kayit(hesap)
        elif secim =="2":
            girisyap = giris(hesap)
            if girisyap:
                print("Giriş başarili.")
                while True:
                    print("\n Bakiye sorgulama [1]")
                    print("\n Para yatirma [2]")
                    print("\n Para çekme [3]")
                    print("\n Çikiş yap [4]")
                    secim2 = input("Lütfen seçiminizi yapınız (1/2/3/4) ")
                    if secim2=="1":
                        bakiyesorgu(hesap,girisyap)
                    elif secim2 == "2":
                        kullanılanbakiye = float(input("Lütfen yatirmak istediğiniz tutari giriniz: "))
                        parayatir(hesap,girisyap,kullanılanbakiye)
                    elif secim2 == "3":
                        kullanılanbakiye = float(input("Çekmek istediğiniz tutarı giriniz: "))
                        paracekme(hesap,girisyap,kullanılanbakiye)
                    elif secim2 == "4":
                        print("Hesaptan Çıkış Yapılıyor...")
                        break
                    else:
                        print("Geçersiz işlem")
            else:
                print("Hatalı İsim veya PIN tekrar deneyiniz.")
        elif secim == "3":
            print("Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Seçim.")

anagiris()