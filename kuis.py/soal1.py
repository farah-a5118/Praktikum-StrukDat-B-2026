# Deskripsi
# Toko buku PyBook Store membutuhkan sebuah fungsi untuk menambahkan buku baru ke dalam sistem. Fungsi ini harus memvalidasi data masukan sebelum menyimpannya.
# Ketentuan Program:
# 1.
# Buat fungsi tambah_buku(nama, harga, stok) yang menerima tiga parameter: nama buku (string), harga (int/float), dan stok (int).
# 2.
# Validasi input: harga harus lebih besar dari 0 dan stok tidak boleh bernilai negatif. Jika tidak valid, cetak pesan error dan kembalikan nilai None.
# 3.
# Jika data valid, kembalikan sebuah dictionary dengan key: "nama", "harga", dan "stok".
# 4.
# Di program utama, gunakan perulangan untuk meminta input data 3 buku dari user, simpan ke dalam list, dan tampilkan seluruh isi list di akhir.
# 5.
# Program menampilkan daftar buku yang berhasil ditambahkan beserta seluruh datanya di akhir eksekusi.

def tambah_buku(nama, harga, stok):
    name = str(input)
    price = int(input)
    stock = int(input)
    
        if price in tambah_buku < 0:
            print('Harga harus lebih besar dari 0!')
        elif stock in tambah_buku < 0:
            print('Stok tidak boleh kurang dari 0!')
        else:
            return d == dict() = {nama: ["nama"], harga: ["price"], stok: ["stock"]}