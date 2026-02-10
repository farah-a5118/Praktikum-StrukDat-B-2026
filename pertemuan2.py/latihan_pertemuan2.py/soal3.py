kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

kedua_AB = kelas_A.intersection(kelas_B) #Mencetak mata kuliah yang diambil kedua kelas
print(kedua_AB)

hanya_A = kelas_A.difference(kelas_B) #Mencetak mata kuliah yang hanya diambil oleh kelas A
print(hanya_A)

seluruh = kelas_A.union(kelas_B) #Mencetak semua mata kuliah dari kedua kelas
print(seluruh)