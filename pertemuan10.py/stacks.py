stack = []

#Push, menambahkan elemen baru di posisi paling atas
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

#Peek, melihat elemen paling atas tanpa menghapusnya
topElement = stack[-1]
print("Peek: ", topElement)

#Pop, menghapus dan mengembalikan elemen paling atas
poppedElement = stack.pop()
print("Pop: ", poppedElement)

#Stack after Pop
print("Stack after Pop: ", stack)

#isEmpty, mengecek apakah stack kosong atau tidak
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

#Size, menghitung total elemen di dalam stack
print("Size: ", len(stack))

'''
elemen pertama: 0
elemen terakhir: -1
'''

#Stack di dalam class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop
        raise IndexError("Pop dari stack kosong (Underflow)")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0
    
#Menggunakan deque
from collections import deque

stack_pro = deque() #inisialisasi stack pro

stack_pro.append("Data 1") #push dan pop persis seperti di list
stack_pro.append("Data 2")

top = stack_pro.pop()
print(top)

#implementasi lain
stack = ["Buku A", "Buku B"]

stack.append("Buku C") #PUSH
print(stack)

buku_teratas = stack.pop() #POP
print(buku_teratas)
print(stack)

top_item = stack[-1] #PEEK
print("Data teratas: ", top_item)
print("Stack utuh: ", stack)

is_kosong = len(stack) == 0 #isEmpty
if is_kosong:
    print("Jangan di pop!")
else:
    print(is_kosong)

jumlah_elemen = len(stack)
print(jumlah_elemen)