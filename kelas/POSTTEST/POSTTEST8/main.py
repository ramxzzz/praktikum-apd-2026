"""Program dealer mobil Aphrodite."""

import os

from auth import login, registrasi
from data import mobil
from menus import menu_admin, menu_pengguna
from tampilan import tampilkan_mobil


def jeda():
    input("Tekan Enter untuk melanjutkan...")


def main():
    berjalan = True

    while berjalan:
        print("\n=== DEALER APHRODITE JUAL BELI MOBIL ===")
        print("1. Login")
        print("2. Register")
        print("3. Lihat stok")
        print("4. Keluar")

        try:
            pilihan = input("Pilihan menu: ").strip()

            if pilihan == "1":
                pengguna = login()

                if pengguna:
                    if pengguna[2] == "admin":
                        menu_admin()
                    else:
                        menu_pengguna(pengguna[0])

            elif pilihan == "2":
                registrasi()

            elif pilihan == "3":
                tampilkan_mobil(mobil)

            elif pilihan == "4":
                berjalan = False
                print("Terima kasih telah berkunjung.")

            else:
                print("Pilihan tidak tersedia.")

            if berjalan:
                jeda()
                os.system("cls" if os.name == "nt" else "clear")

        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan dengan aman.")
            berjalan = False


if __name__ == "__main__":
    main()