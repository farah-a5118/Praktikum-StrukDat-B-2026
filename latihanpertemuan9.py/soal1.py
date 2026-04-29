#Membuat class Node dengan atribut judul, pengarang, next, dan prev
class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

#Membuat class DoubleLinkedList
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    #Menambahkan fungsi penyisipan data
    def insert_tail(self, judul, pengarang):
        nodeBaru = Node(judul, pengarang)

        if self.head is None:
            self.head = nodeBaru
            return
        
        nodeAkhir = self.head
        while nodeAkhir.next:
            nodeAkhir = nodeAkhir.next

        nodeAkhir.next = nodeBaru
        nodeBaru.prev = nodeAkhir

    #Menambahkan fungsi print dari depan
    def print_forward(self):
        nodeAkhir = self.head
        while nodeAkhir:
            print(f"{nodeAkhir.judul} - {nodeAkhir.pengarang}")
            nodeAkhir = nodeAkhir.next

    #Menambahkan fungsi print dari belakang
    def print_backward(self):
        nodeAkhir = self.head
        if nodeAkhir is None:
            return
        
        while nodeAkhir.next:
            nodeAkhir = nodeAkhir.next

        while nodeAkhir:
            print(f"{nodeAkhir.judul} - {nodeAkhir.pengarang}")
            nodeAkhir = nodeAkhir.prev

    #Menambahkan fungsi menghapus berdasarkan judul buku
    def delete_by_judul(self, judul):
        nodeAkhir = self.head

        while nodeAkhir:
            if nodeAkhir.judul == judul:
                if nodeAkhir.prev is None:
                    self.head = nodeAkhir.next
                    if self.head:
                        self.head.prev = None
                else:
                    nodeAkhir.prev.next = nodeAkhir.next
                    if nodeAkhir.next:
                        nodeAkhir.next.prev = nodeAkhir.prev
                return 
            nodeAkhir = nodeAkhir.next

#Menjalankan kode program
doublelinked = DoubleLinkedList()

doublelinked.insert_tail("Laskar Pelangi", "Andrea Hirata")
doublelinked.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
doublelinked.insert_tail("Sang Pemimpi", "Andrea Hirata")

print("Depan:")
doublelinked.print_forward()

print("\nBelakang:")
doublelinked.print_backward()

doublelinked.delete_by_judul("Bumi Manusia")

print("\nSetelah dihapus:")
doublelinked.print_forward()