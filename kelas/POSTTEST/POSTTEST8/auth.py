"""Fungsi login dan registrasi akun."""

from data import akun


def login():
    """Memberi pengguna tiga kesempatan untuk login."""
    for sisa in range(3, 0, -1):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        for data_akun in akun:
            if data_akun[0] == username and data_akun[1] == password:
                print(f"Selamat datang, {username}!")
                return data_akun

        print(f"Username atau password salah. Sisa percobaan: {sisa - 1}.")

    print("Kesempatan login habis. Silakan coba lagi nanti.")
    return None


def registrasi():
    """Mendaftarkan akun pengguna baru."""
    username_baru = input("Buat username: ").strip()
    password_baru = input("Buat password: ").strip()

    if not username_baru or not password_baru:
        print("Username dan password wajib diisi.")
        return

    for data_akun in akun:
        if data_akun[0].lower() == username_baru.lower():
            print("Username sudah digunakan.")
            return

    akun.append([username_baru, password_baru, "pengguna"])
    print("Registrasi berhasil. Silakan login.")