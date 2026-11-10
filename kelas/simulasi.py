mahasiswa = {"nama" : "Nur muqarram Allahu Ash' Sajadah",
              "nim" : "L200180123", 
              "prodi" : "Teknik Informatika",
              "semester" : 1}

mahasiswa["alamat"] = "jl.suryanata bukit pinang"
mahasiswa["email"] = "asepdumang@gmail.com"

mahasiswa["semester"] += 1

print("jumlah item:", len(mahasiswa))

print("isi dictionary:")
for key, value in mahasiswa.items():
          print(f"{key}: {value}")

alamat_dihapus = mahasiswa.pop("alamat")
print("nAlamat dihapus:", alamat_dihapus)
print("dictionary setelah alamat dihapus:", mahasiswa)




            


