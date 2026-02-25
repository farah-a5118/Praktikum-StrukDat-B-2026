# 1.
# Diberikan list nilai mahasiswa: nilai_tugas = [70, 85, 90, 65, 80]
# a.
# Ganti nilai 65 menjadi 75 menggunakan pencarian indeks.
# b.
# Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke terkecil.
# c.
# Tampilkan jumlah total seluruh nilai dalam list tersebut.
# d.
# Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak tampilkan "Tidak ada”.

nilai_tugas = [70, 85, 90, 65, 80]

#Ubah nilai
nilai_tugas[3] = 75
print(nilai_tugas)

#Tambah dan urutkan nilai
nilai_tugas.append(95)
nilai_tugas.sort()
print(nilai_tugas)

#Total semua nilai
total = sum(nilai_tugas)
print(total)

#Tampilkan pesan
for x in nilai_tugas:
    if x == 100:
        print("Ada nilai sempurna")
    else:
        print("Tidak ada")
    break