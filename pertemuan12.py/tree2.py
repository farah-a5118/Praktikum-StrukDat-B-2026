class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #LANGKAH 1
    def insert(self, data):
        new = Node(data)

        #Jika tidak ada root, LANGKAH 2
        if self.root == None:
            self.root = new
            return
        
        #Jika ada root, LANGKAH 3
        p = self.root
        q = self.root

        #LANGKAH 4
        while q != None and new.data != p.data:
            p = q #LANGKAH 5

            #LANGKAH 6
            if new.data < p.data:
                q = p.left
            else: #Jika tidak
                q = p.right

        #LANGKAH 7
        if new.data == p.data:
            print("COBA DIAPAKAN DULU BIAR GAK APA KALI")
            return

        #LANGKAH 8
        if new.data < p.data:
            p.left = new
        else:
            p.right = new

bst = BinarySearchTree()

bst.insert(43)
bst.insert(56)
bst.insert(23)
bst.insert(67)
bst.insert(55)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

in_order(bst.root)