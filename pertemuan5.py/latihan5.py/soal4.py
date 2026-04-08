# 4.
# Diberikan data buku dalam bentuk dictionary:
# transaksi = [
# {"produk": "Buku", "harga": 10000, "jumlah": 3},
# {"produk": "Pena", "harga": 5000, "jumlah": 10},
# {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
# ]
# a.
# Ubah jumlah buku menjadi 8.
# b.
# Tambahkan 2 produk baru.
# c.
# Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan.
# Tampilkan ringkasan seperti ini:
# Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.

transaksi = [
    {"produk": "Buku", "harga": 10000, "jumlah": 3},
    {"produk": "Pena", "harga": 5000, "jumlah": 10},
    {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

#Ubah jumlah buku
transaksi[0]["jumlah"] = 8
print(transaksi)

#Tambah produk baru
transaksi.append({"produk": "Tipe-x", "harga": 3000, "jumlah": 5})
transaksi.append({"produk": "Penggaris", "harga": 5000, "jumlah": 7})
print(transaksi)

#Hitung total pendapatan
for x in transaksi:
    total = (x["harga"]*x["jumlah"])
    print(f"{x["produk"]} | total: {total}")