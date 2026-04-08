# Deskripsi:
# Gabungkan semua komponen dari soal 1 hingga 4 menjadi satu program lengkap PyBook Store dengan menu interaktif berbasis teks. Pada soal ini, semua fungsi dan prosedur yang telah dibuat di soal1.py hingga soal4.py ditulis ulang dan digabungkan dalam satu file soal5.py.
# Ketentuan Program:
# Program menampilkan menu berikut dan berjalan dalam perulangan hingga user memilih menu 5:
# === PyBook Store ===
# 1. Tambah Buku
# 2. Tampilkan Semua Buku
# 3. Beli Buku
# 4. Laporan Penjualan
# 5. Keluar
# 1.
# Menu 1 - Tambah Buku: Gunakan fungsi tambah_buku() dan simpan hasilnya ke dalam list katalog.
# 2.
# Menu 2 - Tampilkan Semua Buku: Tampilkan seluruh isi katalog dalam format tabel yang rapi menggunakan f-string.
# 3.
# Menu 3 - Beli Buku: Gunakan prosedur proses_transaksi(). Simpan setiap transaksi berhasil sebagai tuple (nama_buku, jumlah, total) ke list log_transaksi.

from soal1 import tambah_buku as tb
from soal2 import cari_buku as cb 
from soal3 import proses_transaksi as pt 
from soal4 import hitung_diskon as hd 

