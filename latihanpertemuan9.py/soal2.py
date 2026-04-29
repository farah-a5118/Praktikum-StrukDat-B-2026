#Membuat class Node dengan atribut nama dan next
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

#Membuat class CircularLinkedList
class CircularLinkedList:
    def __init__(self):
        self.head = None

    #Menambahkan fungsi penyisipan data
    def insert_tail(self, nama):
        nodeBaru = Node(nama)

        if self.head is None:
            self.head = nodeBaru
            nodeBaru.next = self.head
            return
        
        nodeAkhir = self.head
        while nodeAkhir.next != self.head:
            nodeAkhir = nodeAkhir.next

        nodeAkhir.next = nodeBaru
        nodeBaru.next = self.head

    #Menambahkan fungsi print antrian
    def print_antrian(self):
        if self.head is None:
            return
        
        nodeAkhir = self.head
        while True:
            print(nodeAkhir.nama, end=" -> ")
            nodeAkhir = nodeAkhir.next
            if nodeAkhir == self.head:
                break
        print("Kembali ke awal")

    #Menambahkan fungsi menghapus head
    def delete_head(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return

        nodeAkhir = self.head
        while nodeAkhir.next != self.head:
            nodeAkhir = nodeAkhir.next

        nodeAkhir.next = self.head.next
        self.head = self.head.next

#Menjalankan kode program
circularlinked = CircularLinkedList()

circularlinked.insert_tail("Andi")
circularlinked.insert_tail("Budi")
circularlinked.insert_tail("Citra")
circularlinked.insert_tail("Dina")

print("Antrian awal:")
circularlinked.print_antrian()

circularlinked.insert_tail("Edo")
print("\nSetelah ditambah Edo:")
circularlinked.print_antrian()

circularlinked.delete_head()
print("\nSetelah Andi selesai dilayani:")
circularlinked.print_antrian()