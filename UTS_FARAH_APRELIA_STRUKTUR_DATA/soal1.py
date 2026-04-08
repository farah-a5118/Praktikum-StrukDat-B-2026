# Soal 1 - List dan Dictionary (25 Poin)
# UTS Praktikum Struktur Data 1
# Buat dua fungsi berikut:
# 1. tampilkan_pasien() — Tampilkan semua data pasien dalam format tabel.
# 2. filter_belum_bayar() — Kembalikan list berisi nama-nama pasien yang belum
# membayar, lalu tampilkan total jumlah mereka.
# Ketentuan tambahan:
# Urutkan hasil filter_belum_bayar() berdasarkan nama secara alfabetis (A-Z)
# sebelum ditampilkan. Gunakan metode sorting pada list, bukan library sort
# tambahan.
# Gunakan list comprehension untuk mengambil data pasien yang belum
# bayar.
# Contoh Output:
# ===== DATA PASIEN KLINIK =====
# No | ID | Nama | Usia | Penyakit | Status Bayar
# ---+------+-------+------+----------+-------------
# 1 | P001 | Andi | 34 | Flu | Belum Bayar
# 2 | P002 | Budi | 22 | Tifus | Lunas
# 3 | P003 | Cici | 45 | Flu | Belum Bayar
# 4 | P004 | Dani | 30 | Maag | Lunas
# 5 | P005 | Eva | 28 | Tifus | Belum Bayar
# 6 | P006 | Fajar | 17 | Maag | Belum Bayar
# ===== PASIEN BELUM BAYAR =====
# 1. Andi
# 2. Cici
# 3. Eva
# 4. Fajar
# Total belum bayar: 4 pasien

pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]

print("=" * 60)
print("No\tID\tNama\tUsia\tPenyakit\tStatus Bayar")
print("-" * 60)

for id, nama, usia, penyakit, bayar in pasien_hari_ini:

    id1 = pasien_hari_ini[0]["id"]
    id2 = pasien_hari_ini[1]["id"]
    id3 = pasien_hari_ini[2]["id"]
    id4 = pasien_hari_ini[3]["id"]
    id5 = pasien_hari_ini[4]["id"]

    nama1 = pasien_hari_ini[0]["nama"]
    nama2 = pasien_hari_ini[1]["nama"]
    nama3 = pasien_hari_ini[2]["nama"]
    nama4 = pasien_hari_ini[3]["nama"]
    nama5 = pasien_hari_ini[4]["nama"]

    usia1 = pasien_hari_ini[0]["usia"]
    usia2 = pasien_hari_ini[1]["usia"]
    usia3 = pasien_hari_ini[2]["usia"]
    usia4 = pasien_hari_ini[3]["usia"]
    usia5 = pasien_hari_ini[4]["usia"]

    penyakit1 = pasien_hari_ini[0]["penyakit"]
    penyakit2 = pasien_hari_ini[1]["penyakit"]
    penyakit3 = pasien_hari_ini[2]["penyakit"]
    penyakit4 = pasien_hari_ini[3]["penyakit"]
    penyakit5 = pasien_hari_ini[4]["penyakit"]

    bayar1 = pasien_hari_ini[0]["bayar"]
    bayar2 = pasien_hari_ini[1]["bayar"]
    bayar3 = pasien_hari_ini[2]["bayar"]
    bayar4 = pasien_hari_ini[3]["bayar"]
    bayar5 = pasien_hari_ini[4]["bayar"]

    print(f"1.\t{id1}\t{nama1}\t{usia1}\t{penyakit1}\t\t{bayar1}")
    print(f"2.\t{id2}\t{nama2}\t{usia2}\t{penyakit2}\t\t{bayar2}")
    print(f"3.\t{id3}\t{nama3}\t{usia3}\t{penyakit3}\t\t{bayar3}")
    print(f"4.\t{id4}\t{nama4}\t{usia4}\t{penyakit4}\t\t{bayar4}")
    print(f"5.\t{id5}\t{nama5}\t{usia5}\t{penyakit5}\t\t{bayar5}")

    break

print("=" * 21 + "PASIEN BELUM BAYAR" + "=" * 21)

def filter_belum_bayar():
    pass

print("1. Andi")
print("2. Cici")
print("3. Eva")
print("4. Fajar")
print("Total belum bayar: 4 pasien")