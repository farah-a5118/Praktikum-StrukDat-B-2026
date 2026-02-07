#Elemen dalam tiple tidak bisa diubah atau unchangeable

thistuple = ("apple", "banana", "cherry")
print(thistuple) #Mencetak semua item di dalam value

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #Mengecek berapa banyak item di dalam tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #Mencetak item di dalam tuple yang memiliki indeks 1

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #Mencetak item dari indeks ke dua sampai empat, karena indeks kelima tidak ikut dihitung

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" #Mengubah item indeks ke 1 di dalam tuple menjadi kiwi
x = tuple(y)

print(x)
