from konverter import konversi as kv #Import fungsi konversi() pada file konverter
from kurs import kurs as ks #Import dictionary kurs pada file kurs
from tabulate import tabulate #Import fungsi tabulate dari library eksternal

print("=== Konverter Mata Uang ===") #Pembatas agar lebih rapi

tabel = [[k, v] for k, v in ks.items()] #List comprehension, buat list [k, v] untuk setiap pasangan (k, v) dalam ks.items()
print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid")) #Membuat tabel dengan module tabulate

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ") #Input nama mata uang yang akan dikonversi
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ") #Input konversi ke mata uang mana
jumlah = float(input("Jumlah: ")) #Input jumlah uang yang akan dikonversi

hasil = kv(jumlah, dari, ke) #Memanggil fungsi pada file konverter

print(f"{int(jumlah)} = {hasil:.2f}") #Mencetak hasil konversi mata uang