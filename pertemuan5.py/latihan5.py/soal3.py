# 3.
# Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:
# sesi_pagi = {"Andi", "Budi", "Cici"} sesi_siang = {"Budi", "Deni", "Eka"}
# a.
# Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang)
# b.
# Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua sesi tanpa duplikat).
# c.
# Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.

sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

#Tampilkan nama hadir semua sesi
hadir_terus = sesi_pagi & sesi_siang
print(hadir_terus)

#Nama unik tanpa duplikat
nama_unik = sesi_pagi | sesi_siang
print(nama_unik)

#Gabungkan set
sesi_pagi.update(sesi_siang)
sesi_hari_ini = sesi_pagi
print(sesi_hari_ini)