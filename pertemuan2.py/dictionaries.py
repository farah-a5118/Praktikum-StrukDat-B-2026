#Dictionary dapat diubah atau changeable dan berurutan

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #Mencetak semua value yang ada di dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #Mencetak value dari variabel brand

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #Mencetak semua value dalam dictionary
print(len(thisdict)) #Menghitung berapa jumlah item yang ada di dalam dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) #Mengecek tipe data, yang bertipe dict

thisdict = dict(name = "John", age = 36, country = "Norway") #Ini adalah versi pendek dari dictionary
print(thisdict) #Mencetak semua value dalam dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values() #Untuk mengecek value yang ada di dalam dictionary, dan akan mengalami perubahan jika item di dalam dict diubah

print(x)

car["year"] = 2020 #Value dalam variabel year akan berubah menjadi 2020

print(x)
