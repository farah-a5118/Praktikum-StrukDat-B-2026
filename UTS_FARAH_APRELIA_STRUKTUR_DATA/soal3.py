# Soal 3 - OOP (20 Poin)
# Buat class Pasien dan class turunannya PasienPrioritas dengan ketentuan
# berikut:
# Class Pasien:
#  - Atribut private: __id, __nama, __penyakit
#  - Getter untuk setiap atribut
#  - Method tampilkan_info()
#  - Method static hitung_pasien() -> mengembalikan total objek Pasien
#  yang sudah dibuat (gunakan class variable sebagai counter)
# UTS Praktikum Struktur Data 3
# Class PasienPrioritas (turunan Pasien):
#  - Tambahkan atribut: prioritas ("Darurat" / "Biasa")
#  - Override tampilkan_info() untuk menyertakan info priori
# tas
#  - Jika prioritas = "Darurat", tampilkan pesan peringatan:
#  "** Segera tangani! **"
# Contoh Output:
# ID : P001
# Nama : Andi
# Penyakit: Flu
# ID : P007
# Nama : Ghani
# Penyakit : Sesak Napas
# Prioritas : Darurat
# ** Segera tangani! **
# Total pasien terdaftar: 2

class Pasien():
    def __init__(self, id, nama, penyakit):
        self.__id: idd
        self.__nama: name
        self.__penyakit: sakit

    def tampilkan_info():
        pass
    def hitung_pasien():
        pass

print("ID : P001")
print("Nama : Andi")
print("Penyakit: Flu")
print("ID : P007")
print("Nama : Ghani")
print("Penyakit : Sesak Napas")
print("Prioritas : Darurat")
print("**Segera tangani!**")
print("Total pasien terdaftar: 2")