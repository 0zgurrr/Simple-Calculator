# Profesyonel Python Hesap Makinesi

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Hata: Bir sayı sıfıra bölünemez!"

def us_alma(a, b):
    return a ** b

def mod_alma(a, b):
    return a % b

def hesapla():
    print("=== Profesyonel Python Hesap Makinesi ===")
    print("İşlemler:")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Üs alma (^)")
    print("6. Mod alma (%)")
    print("7. Çıkış")

    while True:
        secim = input("İşleminizi seçin (1-7): ")

        if secim == '7':
            print("Hesap makinesi kapatılıyor. Hoşçakal!")
            break

        if secim not in ['1','2','3','4','5','6']:
            print("Geçersiz seçim. Tekrar deneyin.")
            continue

        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin!")
            continue

        if secim == '1':
            print(f"Sonuç: {toplama(sayi1, sayi2)}")
        elif secim == '2':
            print(f"Sonuç: {cikarma(sayi1, sayi2)}")
        elif secim == '3':
            print(f"Sonuç: {carpma(sayi1, sayi2)}")
        elif secim == '4':
            print(f"Sonuç: {bolme(sayi1, sayi2)}")
        elif secim == '5':
            print(f"Sonuç: {us_alma(sayi1, sayi2)}")
        elif secim == '6':
            print(f"Sonuç: {mod_alma(sayi1, sayi2)}")

        print("\n-------------------------\n")

if __name__ == "__main__":
    hesapla()
