#Elemen dalam list dapat diubah atau changeable

mylist = ["Durian", "Mangga", "Pepaya"]
print(mylist) #Untuk mencetak semua item di dalam list
print(len(mylist)) #Untuk mengecek berapa banyak item di dalam list, bukan indeks

mylist = ["abc", 34, True, 40, False]
print(mylist) #Untuk mencetak semua item di dalam list

thislist = (("Pisang", "Manggis", "Pir", "Apel"))
print(thislist) #Mencetak semua item dalam list

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #Menambahkan item watermelon ke dalam list pada indeks kedua
print(thislist) #Mencetak item di dalam list yang sudah diperbarui

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #Menambahkan item orange di akhir list
print(thislist) #Mencetak item di list yang sudah diperbarui

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #Menginput semua item yang berada di list tropical ke dalam this list
print(thislist) #Mencetak list

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #Menghapus item banana dari dalam list, namun hanya salah satu, yaitu yang terletak di awal list
print(thislist) #Mencetak list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Menghapus item di dalam list secara random
print(thislist) #Mencetak list

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): #Melakukan perulangan pada list, ini akan mencetak semua item berdasarkan indeks angkanya secara berurutan
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist): #Menggunakan while loops untuk melakukan perulangan pada list secara berurutan berdasarkan indeks
  print(thislist[i])
  i = i + 1 #i atau indeks akan ditambah 1 setiap perulangan

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [] #Sebuah list baru yang nantinya akan diisi

for x in fruits:
  if "a" in x: #List yang baru hanya akan berisi item yang memiliki huruf a di dalamnya
    newlist.append(x) #Mengisi newlist dengan item yang dimaksud

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] #Ini adalah versi shorthand atau versi pendek dari pengisian list baru

print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #Mengurutkan item di dalam list berdasarkan alfabet
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #Mengurutkan angka di dalam list mulai dari yang tertinggi
print(thislist)

def myfunc(n):
  return abs(n - 50) #50 adalah angka yang menjadi acuan

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #Mengurutkan angka mulai dari yang lebih dekat dengan 50
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #Membalikkan urutan item di dalam list
print(thislist)
