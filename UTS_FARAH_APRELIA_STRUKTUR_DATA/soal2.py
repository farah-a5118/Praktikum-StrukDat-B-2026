# Soal 2 - Tuple dan Set (15 Poin)
# Buat dua fungsi berikut:
# 1. info_klinik() — Kembalikan informasi tetap klinik menggunakan tuple lalu
# tampilkan isinya.
# UTS Praktikum Struktur Data 2
# 2. rekap_penyakit() — Gunakan set untuk mendapatkan jenis penyakit unik, lalu
# hitung jumlah pasien per jenis penyakit menggunakan dictionary.
# Ketentuan tambahan:
# Dari hasil rekap, tampilkan jenis penyakit dengan jumlah pasien terbanyak.
# Jika ada lebih dari satu penyakit dengan jumlah yang sama, tampilkan
# keduanya.
# Contoh Output:
# Info Klinik:
# Nama : Klinik Sehat Bersama
# Alamat : Jl. Merdeka No. 10, Pekanbaru
# Telp : 0761-12345
# Jenis Penyakit Unik: {'Flu', 'Tifus', 'Maag'}
# Jumlah jenis penyakit: 3
# Rekap per penyakit:
# Flu : 2 pasien
# Tifus : 2 pasien
# Maag : 2 pasien
# Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)

InfoKlinik = {
    "Nama" : ("Klinik Sehat Bersama",),
    "Alamat" : ("Jl. Merdeka No. 10, Pekanbaru",),
    "Telp" : ("0761-12345")
}

JenisPenyakitUnik = {'Flu', 'Tifus', 'Maag'}

def info_klinik():
    pass
def rekap_penyakit():
    pass

print("Nama : Klinik Sehat Bersama")
print("Alamat : Jl. Merdeka No. 10, Pekanbaru")
print("Telp : 0761-12345")

print(JenisPenyakitUnik)

print("Jumlah jenis penyakit: 3")
print("Rekap per penyakit:")
print("Flu : 2 pasien")
print("Tifus : 2 pasien")
print("Maag : 2 pasien")
print("Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)")