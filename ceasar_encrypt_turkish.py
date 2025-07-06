def caesar_encrypt_turkish(text, shift):
    turkce_kucuk = "abcçdefgğhıijklmnoöprsştuüvyz"
    turkce_buyuk = turkce_kucuk.upper()


    shift = shift % len(turkce_kucuk)
    result = []


    for char in text:
        if char in turkce_kucuk:
            idx = turkce_kucuk.index(char)
            new_idx = (idx + shift) % len(turkce_kucuk)
            result.append(turkce_kucuk[new_idx])
        elif char in turkce_buyuk:
            idx = turkce_buyuk.index(char)
            new_idx = (idx + shift) % len(turkce_buyuk)
            result.append(turkce_buyuk[new_idx])
        else:
            result.append(char)
    return "".join(result)


def caesar_decrypt_turkish(text, shift):
    return caesar_encrypt_turkish(text, -shift)


while True:
    print("\n1: Şifrele\n2: Çöz\nq: Çıkış")
    secim = input("Seçiminiz: ")
    if secim == "q":
        print("Programdan çıkılıyor...")
        break
    if secim not in ["1", "2"]:
        print("Geçersiz seçim!")
        continue


    metin = input("Metni girin: ")
    try:
        kaydirma = int(input("Kaydırma sayısını girin: "))
    except ValueError:
        print("Geçersiz kaydırma sayısı!")
        continue


    if secim == "1":
        sonuc = caesar_encrypt_turkish(metin, kaydirma)
        print("Şifreli metin:", sonuc)
    else:
        sonuc = caesar_decrypt_turkish(metin, kaydirma)
        print("Çözülmüş metin:", sonuc)
