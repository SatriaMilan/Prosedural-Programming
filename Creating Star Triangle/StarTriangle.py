def segitiga_sama_kaki(tinggi):
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)

def segitiga_sama_kaki_terbalik(tinggi):
    for i in range(tinggi, 0, -1):
        spasi = " " * (tinggi - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)

def segitiga_siku_siku(tinggi):
    for i in range(1, tinggi + 1):
        print("*" * i)

def segitiga_siku_siku_terbalik(tinggi):
    for i in range(tinggi, 0, -1):
        print("*" * i)

while True:
    print("Menu:")
    print("1. Sama Kaki")
    print("2. Sama Kaki Terbalik")
    print("3. Siku Siku")
    print("4. Siku Siku Terbalik")
    print("0. Keluar")
    
    choice = input("Masukkan pilihan Anda: ")
    
    if choice == "1":
        tinggi = int(input("Masukkan tinggi segitiga sama kaki: "))
        segitiga_sama_kaki(tinggi)
    elif choice == "2":
        tinggi = int(input("Masukkan tinggi segitiga sama kaki terbalik: "))
        segitiga_sama_kaki_terbalik(tinggi)
    elif choice == "3":
        tinggi = int(input("Masukkan tinggi segitiga siku-siku: "))
        segitiga_siku_siku(tinggi)
    elif choice == "4":
        tinggi = int(input("Masukkan tinggi segitiga siku-siku terbalik: "))
        segitiga_siku_siku_terbalik(tinggi)
    elif choice == "0":
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid")
