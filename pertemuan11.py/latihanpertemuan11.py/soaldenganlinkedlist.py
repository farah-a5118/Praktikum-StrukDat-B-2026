class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class SehatBersama:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1
        print(f"Enqueue: {nama, keluhan}")

    def dequeue(self):
        if self.is_empty():
            return "Antrian kosong!"
    
        temp = (self.front.nama, self.front.keluhan)
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        return temp
    
    def peek(self):
        if self.is_empty():
            return "Antrian kosong!"
        return (self.front.nama, self.front.keluhan)
    
    def size(self):
        return self.count
    
daftarpasien = SehatBersama()

print("\nApakah antrian kosong?: ", daftarpasien.is_empty())

daftarpasien.enqueue('BUDI', 'Demam Tinggi')
daftarpasien.enqueue('ANI', 'Batuk Pilek')
daftarpasien.enqueue('CITRA', 'Sakit Kepala')

print("\nJumlah pasien yang menunggu: ", daftarpasien.size())
print("Antrian paling depan: ", daftarpasien.peek())
print("Pasien pertama: ", daftarpasien.dequeue())

daftarpasien.enqueue('\nDODI', 'Sakit Perut')

print("\nPasien berikutnya: ", daftarpasien.dequeue())
print("\nJumlah pasien yang menunggu: ", daftarpasien.size())