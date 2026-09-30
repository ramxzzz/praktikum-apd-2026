
#          SISTEM TOP UP GAME


print("=" * 45)
print("        SISTEM TOP UP GAME")
print("=" * 45)


# LOGIN


username_benar = "aphrodite"
password_benar = "84"   # 2 digit NIM

print("\n--- LOGIN ---")

username = input("Username : ")
password = input("Password : ")

# Validasi login
if username == username_benar and password == password_benar:

    print("\nLogin Berhasil!")

    # MENU TOP UP

    print("\n" + "=" * 45)
    print("           MENU TOP UP")
    print("=" * 45)

    id_player = input("ID Player : ")

    print("\nPilihan Game:")
    print("1. Genshin Impact")
    print("2. Minecraft")
    print("3. Mobile Legends")

    nama_game = input("Nama Game : ")

    print("\nKategori Top Up:")
    print("1. Kecil    = Rp15.000")
    print("2. Menengah = Rp50.000")
    print("3. Besar    = Rp150.000")

    kategori = input("Kategori Top Up : ")

    print("\nMetode Pembayaran:")
    print("1. Pulsa")
    print("2. E-Wallet")

    pembayaran = input("Metode Pembayaran : ")

     # MENENTUKAN HARGA TOP UP

    if kategori.lower() == "kecil":
        harga_dasar = 15000

    elif kategori.lower() == "menengah":
        harga_dasar = 50000

    elif kategori.lower() == "besar":
        harga_dasar = 150000

    else:
        print("\nKategori Top Up tidak valid!")
        exit()

    
    # BIAYA ADMIN
    # TERNARY OPERATOR
    

    biaya_admin = 2500 if pembayaran.lower() == "pulsa" else 500

    # Validasi metode pembayaran
    if pembayaran.lower() != "pulsa" and pembayaran.lower() != "e-wallet":
        print("\nMetode pembayaran tidak valid!")
        exit()

   
    # TOTAL PEMBAYARAN

    total_bayar = harga_dasar + biaya_admin

    print("\n" + "=" * 45)
    print("        TOTAL PEMBAYARAN")
    print("=" * 45)

    print(f"Harga Top Up : Rp{harga_dasar:,}".replace(",", "."))
    print(f"Biaya Admin  : Rp{biaya_admin:,}".replace(",", "."))
    print(f"Total Bayar  : Rp{total_bayar:,}".replace(",", "."))

    print("=" * 45)

   
    # PEMBAYARAN
    

    uang_bayar = int (input("Uang Dibayarkan : Rp"))

    # Validasi pembayaran
    if uang_bayar < total_bayar:

        
        print("        TRANSAKSI GAGAL")
        print("Saldo tidak mencukupi.")
        print(f"Uang Kurang : Rp{total_bayar - uang_bayar:,}".replace(",", "."))

    else:

        kembalian = uang_bayar - total_bayar
        print("Tranksaksi berhasil!")
        print("kembalian :", kembalian)

        # STRUK PEMBELIAN
        
        print("\n")
        print("=" * 45)
        print("           STRUK PEMBELIAN")
        print("=" * 45)

        print(f"ID Player        : {id_player}")
        print(f"Nama Game        : {nama_game}")
        print(f"Kategori Top Up  : {kategori}")
        print(f"Metode Pembayaran: {pembayaran}")
        print(f"Biaya Admin      : Rp{biaya_admin:,}".replace(",", "."))
        print(f"Total Bayar      : Rp{total_bayar:,}".replace(",", "."))
        print(f"Uang Dibayar     : Rp{uang_bayar:,}".replace(",", "."))
        print(f"Kembalian        : Rp{kembalian:,}".replace(",", "."))

        print("=" * 45)
        print("        TRANSAKSI BERHASIL!")
        print("          Terima Kasih")
        print("=" * 45)

else:

    print("             LOGIN GAGAL")
    print("Username atau Password salah.")
    print("Program berakhir.")
