while True:
    print("Menu:")
    print("1. Sama Kaki")
    print("2. Sama Kaki terbalik")
    print("3. Siku siku")
    print("4. Siku-siku terbalik")
    print("0. Keluar")
    choice = input("Masukkan pilihan Anda: ")
 
    if choice == "1":
        print("Anda memilih Segitiga Sama Kaki")
    elif choice == "2":
        print("Anda memilih Segitiga Sama Kaki terbalik")
    elif choice == "3":
        print("Anda memilih Segitiga siku-siku")
    elif choice == "4":
        print("Anda memilih Segitiga siku-siku terbalik")
    elif choice == "0":
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid")