"""Menu admin dan pengguna untuk program dealer mobil."""

from datetime import datetime

from data import mobil, riwayat_transaksi
from tampilan import rupiah, tampilkan_mobil, tampilkan_transaksi


def baca_bilangan(pesan, minimum=0):
    """Meminta input bilangan bulat dan memeriksa nilai minimumnya."""
    while True:
        try:
            angka = int(input(pesan).strip())

            if angka < minimum:
                print(f"Nilai minimal {minimum}.")
            else:
                return angka

        except ValueError:
            print("Input harus berupa bilangan bulat. Coba lagi.")


def cari_mobil(id_mobil):
    """Mencari data mobil berdasarkan ID."""
    for data_mobil in mobil:
        if data_mobil[0] == id_mobil:
            return data_mobil

    return None


def konfirmasi_aksi(pesan):
    """Meminta konfirmasi y/t."""
    jawaban = input(f"{pesan} (y/t): ").strip().lower()
    return jawaban == "y"


def menu_admin():
    """Menampilkan menu khusus admin."""
    id_berikutnya = max(
        (data_mobil[0] for data_mobil in mobil),
        default=0
    ) + 1

    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat stok")
        print("2. Tambah mobil")
        print("3. Ubah mobil")
        print("4. Hapus mobil")
        print("5. Lihat transaksi")
        print("6. Logout")

        pilihan = input("Pilih: ").strip()

        try:
            if pilihan == "1":
                tampilkan_mobil(mobil)

            elif pilihan == "2":
                merek = input("Merek: ").strip()
                model = input("Model: ").strip()

                if not merek or not model:
                    print("Merek dan model wajib diisi.")
                    continue

                tahun = baca_bilangan("Tahun: ", 1886)
                harga = baca_bilangan("Harga: ", 1)
                stok = baca_bilangan("Stok: ", 0)

                mobil.append([
                    id_berikutnya,
                    merek,
                    model,
                    tahun,
                    harga,
                    stok,
                ])

                print(f"Mobil ditambahkan dengan ID {id_berikutnya}.")
                id_berikutnya += 1

            elif pilihan == "3":
                tampilkan_mobil(mobil)
                id_mobil = baca_bilangan("ID mobil yang diubah: ", 1)
                target = cari_mobil(id_mobil)

                if target is None:
                    print("ID tidak ditemukan.")
                    continue

                merek_baru = input(
                    "Merek baru (Enter untuk tetap): "
                ).strip()
                model_baru = input(
                    "Model baru (Enter untuk tetap): "
                ).strip()

                if merek_baru:
                    target[1] = merek_baru
                if model_baru:
                    target[2] = model_baru

                perubahan_angka = [
                    (3, "Tahun", 1886),
                    (4, "Harga", 1),
                    (5, "Stok", 0),
                ]

                for indeks, label, minimum in perubahan_angka:
                    teks = input(
                        f"{label} baru (Enter untuk tetap): "
                    ).strip()

                    if teks:
                        try:
                            angka = int(teks)

                            if angka < minimum:
                                raise ValueError

                            target[indeks] = angka
                        except ValueError:
                            print(
                                f"{label} tidak valid; "
                                "nilai lama dipertahankan."
                            )

                print("Data mobil diperbarui.")

            elif pilihan == "4":
                tampilkan_mobil(mobil)
                id_mobil = baca_bilangan("ID mobil yang dihapus: ", 1)
                target = cari_mobil(id_mobil)

                if target is None:
                    print("ID tidak ditemukan.")
                elif konfirmasi_aksi(
                    f"Hapus {target[1]} {target[2]}?"
                ):
                    mobil.remove(target)
                    print("Mobil berhasil dihapus.")

            elif pilihan == "5":
                tampilkan_transaksi(riwayat_transaksi)

            elif pilihan == "6":
                print("Admin berhasil logout.")
                return

            else:
                print("Pilihan tidak tersedia.")

        except (ValueError, EOFError) as error:
            print(f"Kesalahan input: {error}")


def menu_pengguna(username):
    """Menampilkan menu untuk melihat stok dan membeli mobil."""
    while True:
        print("\n=== MENU PENGGUNA ===")
        print("1. Lihat stok")
        print("2. Beli mobil")
        print("3. Logout")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            tampilkan_mobil(mobil)

        elif pilihan == "2":
            try:
                tampilkan_mobil(mobil)
                id_mobil = baca_bilangan("ID mobil: ", 1)
                target = cari_mobil(id_mobil)

                if target is None:
                    print("ID mobil tidak ditemukan.")
                    continue

                if target[5] == 0:
                    print("Stok mobil habis.")
                    continue

                jumlah = baca_bilangan("Jumlah yang dibeli: ", 1)

                if jumlah > target[5]:
                    print(f"Stok tidak mencukupi. Stok tersedia: {target[5]}.")
                    continue

                total = jumlah * target[4]

                if konfirmasi_aksi(
                    f"Total {rupiah(total)}. Lanjutkan pembelian?"
                ):
                    target[5] -= jumlah

                    riwayat_transaksi.append([
                        username,
                        f"{target[1]} {target[2]}",
                        jumlah,
                        total,
                        datetime.now().strftime("%Y-%m-%d %H:%M"),
                    ])

                    print(
                        f"Pembelian berhasil. Total: {rupiah(total)}; "
                        f"sisa stok: {target[5]}."
                    )

            except (ValueError, EOFError) as error:
                print(f"Kesalahan input: {error}")

        elif pilihan == "3":
            print("Terima kasih, silakan datang kembali.")
            return

        else:
            print("Pilihan tidak tersedia.")