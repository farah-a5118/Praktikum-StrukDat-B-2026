#Set tidak bisa diubah atau unchangeable, namun bisa ditambah dan dihapus

thisset = {"apple", "banana", "cherry"}
print(thisset) #Mencetak semua item di dalam set

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #Set tidak bisa memiliki dua item yang sama persis, jadi apple dalam indeks terakhir tidak akan dicetak

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) #True dan 1 akan dianggap sebagai nilai yang sama, oleh sebab itu 1 tidak akan dicetak

thisset = {"apple", "banana", "cherry"}

for x in thisset: #Melakukan perulangan pada set
  print(x) #Mencetak semua item di dalam set, namun tidak berurutan

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #Hanya untuk mengecek apakah banana ada di dalam set, dan akan mengembalikan True

thisset = {"apple", "banana", "cherry"}

thisset.add("orange") #Menambahkan orange di dalam set dengan indeks acak

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist) #Memasukkan semua item dalam list mylist ke dalam thisset

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #Menghapus item banana dari dalam set

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #Menghapus banana dari dalam set

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() #Menghapus item dari dalam set secara random

print(x)

print(thisset)
