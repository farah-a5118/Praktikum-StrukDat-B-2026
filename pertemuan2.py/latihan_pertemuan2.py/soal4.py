mahasiswa = {
    "AOO1": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "AOO2": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "AOO3": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

for x in mahasiswa:
    if (mahasiswa[x]["ipk"]) > 3.5: #Memilih mahasiswa yang memiliki IPK > 3.50
        print(mahasiswa[x]["nama"])

#Rata-rata IPK seluruh mahasiswa
jumlah = 0
hitung = 0
for x in mahasiswa : 
    jumlah = jumlah + (mahasiswa[x]["ipk"]) 
    hitung = hitung + 1
    rata = jumlah/hitung 
print(format(rata, ".2f"))

#Menambahkan data baru ke dictionary
mahasiswa.update({"nama": "Farah", "prodi": "Teknik Informatika", "ipk": 3.46})
print(mahasiswa)