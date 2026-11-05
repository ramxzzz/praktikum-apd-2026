"""Fungsi untuk menampilkan tabel dan harga."""

from prettytable import PrettyTable


def rupiah(nilai):
    return f"Rp {nilai:,}".replace(",", ".")


def tampilkan_mobil(mobil):
    if not mobil:
        print("Stok mobil kosong.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Merek", "Model", "Tahun", "Harga", "Stok"]
    tabel.align = "l"

    for data_mobil in mobil:
        tabel.add_row([
            data_mobil[0],
            data_mobil[1],
            data_mobil[2],
            data_mobil[3],
            rupiah(data_mobil[4]),
            data_mobil[5],
        ])

    print(tabel)


def tampilkan_transaksi(riwayat):
    if not riwayat:
        print("Belum ada transaksi.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["Waktu", "Pembeli", "Mobil", "Jumlah", "Total"]
    tabel.align = "l"

    for transaksi in riwayat:
        tabel.add_row([
            transaksi[4],
            transaksi[0],
            transaksi[1],
            transaksi[2],
            rupiah(transaksi[3]),
        ])

    print(tabel)