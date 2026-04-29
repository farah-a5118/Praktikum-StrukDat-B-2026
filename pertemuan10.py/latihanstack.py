# 1. Simulasi Riwayat Navigasi Browser
# Skenario: Bayangkan Anda adalah seorang Software Engineer yang ditugaskan
# untuk membuat sistem "Riwayat Navigasi" (Browser History) sederhana. Setiap kali
# pengguna mengunjungi halaman web baru, URL halaman tersebut akan ditumpuk.
# Jika pengguna menekan tombol "Back", halaman terakhir akan dihapus dari riwayat
# dan pengguna kembali ke halaman sebelumnya.
# Sistem ini sangat cocok menggunakan struktur data Stack (LIFO - Last In First
# Out).
# Tugas Anda: Anda diminta untuk mengimplementasikan sistem ini menggunakan
# dua cara yang berbeda:
# 1. Menggunakan List biasa (Dynamic Array) bawaan Python.
# 2. Menggunakan Linked List.
# Kedua implementasi tersebut wajib memiliki 5 operasi dasar Stack berikut:
# 1. is_empty(): Memeriksa apakah riwayat kosong (mengembalikan True atau
# False).
# 2. push(url): Menambahkan URL baru ke posisi teratas (pengguna membuka
# halaman baru).
# 3. pop(): Menghapus dan mengembalikan URL di posisi teratas (pengguna
# menekan tombol 'Back'). Jika kosong, kembalikan teks "Riwayat kosong".
# 4. peek(): Melihat URL yang ada di posisi teratas tanpa menghapusnya (melihat
# halaman yang sedang aktif). Jika kosong, kembalikan None.
# 5. size(): Menghitung total URL yang tersimpan di dalam riwayat saat ini.
# Instruksi Pengerjaan
# Untuk mempermudah, lengkapilah kerangka kode (skeleton code) di bawah ini.
# Tuliskan logika Anda pada bagian yang ditandai dengan komentar # Tulis kode di
# sini.
# Bagian 1: Implementasi Menggunakan List Biasa
# class StackList:
# def __init__(self):
# self.items = [] # Menggunakan list bawaan Python
# def is_empty(self):
# # Tulis kode di sini
# pass
# def push(self, url):
# # Tulis kode di sini (Petunjuk: gunakan append)
# pass
# def pop(self):
# # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
# pass
# def peek(self):
# # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
# pass
# def size(self):
# # Tulis kode di sini (Petunjuk: gunakan len())
# pass
# Bagian 2: Implementasi Menggunakan Linked List
# class Node:
# def __init__(self, url):
# self.url = url
# self.next = None
# class StackLinkedList:
# def __init__(self):
# self.top = None
# self.count = 0 # Variabel bantuan untuk melacak ukuran
# def is_empty(self):
# # Tulis kode di sini (Petunjuk: periksa apakah top bernilai None)
# pass
# def push(self, url):
# # Tulis kode di sini
# # 1. Buat Node baru
# # 2. Hubungkan 'next' node baru ke 'top' saat ini
# # 3. Jadikan node baru sebagai 'top' yang baru
# # 4. Tambahkan nilai 'count'
# pass
# def pop(self):
# # Tulis kode di sini
# # 1. Periksa is_empty()
# # 2. Simpan url dari 'top' saat ini
# # 3. Geser 'top' ke node berikutnya (top = top.next)
# # 4. Kurangi nilai 'count'
# # 5. Kembalikan url yang disimpan
# pass
# def peek(self):
# # Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
# pass
# def size(self):
# # Tulis kode di sini (Petunjuk: kembalikan nilai variabel 'count')
# pass

#JAWABAN

#1 Implementasi dengan list biasa
class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if not self.is_empty():
            return self.items.pop

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

Stack = StackList()

Stack.push("https://W3Schools.com")
Stack.push("https://Google.com")
Stack.push("https://Brainly.com")

print("Stack:", Stack.items)
print("Is Empty?", Stack.is_empty())
print("Pop:", Stack.pop())
print("Peek:", Stack.peek())
print("Size:", Stack.size())

#2, Implementasi dengan linked list
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

myStack = Stack()

myStack.push("https://W3Schools.com")
myStack.push("https://Google.com")
myStack.push("https://Brainly.com")

print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())