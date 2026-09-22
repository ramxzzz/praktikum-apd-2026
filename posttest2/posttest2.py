#1. Daftar harga komponen roket
komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

# poin plus: Memasukkan semua komponen kedalam sebuah list harga_komponen
harga_komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]
# biaya administrasi
biaya_administrasi = 15000
# 2. hitung total biaya secara manual (tanpa menggunakan fungsi sum())
total_biaya = komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + biaya_administrasi

# 3. hitung rata-rata harga (total biaya dibagi jumlah data mengunakan len)
rata_rata_harga = total_biaya / len(harga_komponen)

 # 4. variabel NIM (silahkan ganti dengan "19" dengan 2 2 digit terakhir NIM anda)
NIM = "84"

# 5.Variabel boolean untuk mnenentukan apakah  NIM tidak sama dengan rata-rata
bolean = NIM != rata_rata_harga

# poin plus: konversi total biaya ke poundsterling
# kurs perkiraan : 1 GBP = Rp.20.500
kurs_gbp = 20500
total_biaya_gbp = total_biaya / kurs_gbp

# 6. Menampilkan semua variabel ke layar
print("--- RINCINAN BIAYA PEMBELIAN KOMPONEN ---:")
print("Total Biaya: Rp.", total_biaya)
print("Rata-rata Harga: Rp.", rata_rata_harga)
print("NIM: ", NIM)
print("Boolean (NIM != Rata-rata): ", bolean)
print("Total Biaya (GBP): £", total_biaya_gbp)

# poin plus: Menampilkan komponen 1 sampai 4 menggunakan slice index negatif
# Index negatif -6 adalah komponen_1 dan -2 adalah batas akhir (komponen_5, tidak termasuk)
print("Komponen 1 sampai 4 (slice index negatif):", harga_komponen[-6:-2])