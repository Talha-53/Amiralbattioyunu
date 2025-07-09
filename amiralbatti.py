import random

BOYUT = 5
GEMI_SAYISI = 3
CAN = 3
HARFLER = ['A', 'B', 'C', 'D', 'E']

def oyun():
    # Tahtalar
    bilgisayar_tahta = [["-" for _ in range(BOYUT)] for _ in range(BOYUT)]
    gorunen_tahta = [["-" for _ in range(BOYUT)] for _ in range(BOYUT)]
    oyuncu_tahta = [["-" for _ in range(BOYUT)] for _ in range(BOYUT)]

    # Oyuncu gemisi sabit (ortada)
    oyuncu_tahta[2][2] = "G"
    oyuncu_tahta[0][0] = "G"
    oyuncu_tahta[4][4] = "G"

    def gemileri_yerlestir():
        gemiler = 0
        while gemiler < GEMI_SAYISI:
            x = random.randint(0, BOYUT - 1)
            y = random.randint(0, BOYUT - 1)
            if bilgisayar_tahta[y][x] != "G":
                bilgisayar_tahta[y][x] = "G"
                gemiler += 1

    def tahta_yazdir(tahta):
        print("   " + " ".join(HARFLER))
        for i, satir in enumerate(tahta):
            print(f"{i+1}  " + " ".join(satir))

    def koordinat_al():
        while True:
            yatay = input("Yatay (A-E): ").upper()
            dikey = input("Dikey (1-5): ")
            if yatay in HARFLER and dikey.isdigit():
                x = HARFLER.index(yatay)
                y = int(dikey) - 1
                if 0 <= x < BOYUT and 0 <= y < BOYUT:
                    return x, y
            print("Geçersiz koordinat. Örnek: B3")

    def oyuncu_atis():
        x, y = koordinat_al()
        if gorunen_tahta[y][x] != "-":
            print("Daha önce buraya atış yaptın.")
            return False
        elif bilgisayar_tahta[y][x] == "G":
            print("İsabet!")
            gorunen_tahta[y][x] = "X"
            return True
        else:
            print("Iska.")
            gorunen_tahta[y][x] = "O"
            return False

    def bilgisayar_atis(can, vurulanlar):
        while True:
            x = random.randint(0, BOYUT - 1)
            y = random.randint(0, BOYUT - 1)
            if (x, y) not in vurulanlar:
                vurulanlar.add((x, y))
                if oyuncu_tahta[y][x] == "G":
                    print(f"Bilgisayar {HARFLER[x]}{y+1} noktasına saldırdı ve isabet etti!")
                    oyuncu_tahta[y][x] = "X"
                    return can - 1
                else:
                    print(f"Bilgisayar {HARFLER[x]}{y+1} noktasına saldırdı ve ıskaladı.")
                    return can

    # Oyun başlangıcı
    gemileri_yerlestir()
    kalan = GEMI_SAYISI
    can = CAN
    toplam_atis = 0
    isabet_sayisi = 0
    bilgisayar_saldirdigi = set()

    print("\n--- BattleTabs: Gelişmiş Terminal Sürümü ---")
    while kalan > 0 and can > 0:
        print("\nRakip Tahta:")
        tahta_yazdir(gorunen_tahta)
        print(f"Kalan gemi: {kalan} | Can: {can}")
        if oyuncu_atis():
            kalan -= 1
            isabet_sayisi += 1
        toplam_atis += 1
        if kalan == 0:
            break
        can = bilgisayar_atis(can, bilgisayar_saldirdigi)

    print("\n--- Oyun Bitti ---")
    if can == 0:
        print("Tüm canların tükendi. Kaybettin.")
    else:
        print("Tüm düşman gemileri batırıldı. Kazandın!")

    oran = round((isabet_sayisi / toplam_atis) * 100, 2)
    print(f"\nToplam atış: {toplam_atis}")
    print(f"İsabet sayısı: {isabet_sayisi}")
    print(f"Başarı oranı: %{oran}")

def tekrar_oyna():
    while True:
        cevap = input("\nTekrar oynamak ister misin? (Evet/Hayır): ").lower()
        if cevap in ["evet", "e"]:
            return True
        elif cevap in ["hayır", "h"]:
            return False
        else:
            print("Lütfen 'Evet' veya 'Hayır' şeklinde cevap ver.")

# Ana döngü
while True:
    oyun()
    if not tekrar_oyna():
        print("Çıkılıyor...")
        break
# İncelediğiniz için teşekkürler ...