angka = [10, 20, 30, 40, 50]

angka.insert(4, 60) #Menambah angka 60 pada indeks ke 4
angka.remove(20) #Menghapus angka 20
print(angka)

#Menampilkan angka tertinggi dan terendah
print(max(angka)) #Menampilkan angka tertinggi, 60
print(min(angka)) #Menampilkan angka terendah, 10

#Menampilkan Rata-rata
def rata(angka):
    total = sum(angka) #Menjumlahkan total angka
    rata = total/len(angka) #Mencari rata-rata angka
    return rata

angka = [10, 30, 40, 60, 50] #Pemanggilan parameter
hasil = rata(angka)

print(f"Rata-rata: {hasil}") #Outputnya adalah 38.0