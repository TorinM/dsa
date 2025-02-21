class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.size = 0

        self.head = None
        self.tail = None

    def __str__(self):
        ret = []

        trav = self.head
        while trav != None:
            ret.append(trav.data)
            trav = trav.next

        return str("HEAD -> " + " <-> ".join(str(x) for x in ret) + " <- TAIL")
    
    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        trav = self.head

        while trav != None:
            next_node = trav.next # tmp
            trav.prev = None
            trav.next = None
            trav.data = None
            trav = next_node
        
        trav = None
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, val):
        if self.is_empty():
            self.head = self.tail = Node(val, None, None)
        else:
            self.head.prev = Node(val, None, self.head)
            self.head = self.head.prev

        self.size += 1

    def add_last(self, val):
        if self.is_empty():
            self.head = self.tail = Node(val, None, None)
        else:
            self.tail.next = Node(val, self.tail, None)
            self.tail = self.tail.next

        self.size += 1

    def add(self, val):
        self.add_last(val)

    def peek_first(self):
        if self.is_empty(): raise Exception("Empty list")

        return self.head.data
    
    def remove_first(self):
        if self.is_empty(): raise Exception("Empty list")

        data = self.head.data

        self.head = self.head.next

        self.size -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        
        return data
    
    def remove_last(self):
        if self.is_empty(): raise Exception("Empty list")

        data = self.tail.data

        self.tail = self.tail.prev

        self.size -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        
        return data

    def remove_middle(self, node):
        if node.next == None:
            return self.remove_last()
        if node.prev == None:
            return self.remove_first()

        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data

        self.size -= 1

        return data
    
    def remove_by_index(self, idx):
        if idx < 0 or idx >= self.size: raise IndexError("Index out of range")

        # search from front
        if idx < (self.size/2):
            trav = self.head
            for i in range(self.size//2):
                if i == idx: break

                trav = trav.next
        # search from back
        else:
            trav = self.tail
            for i in range(self.size-1, self.size//2, -1):
                if i == idx: break

                trav = trav.prev
        
        return self.remove_middle(trav)
    
    def remove_by_val(self, val):
        trav = self.head

        while trav != None:
            if trav.data == val:
                self.remove_middle(trav)
                return True

            trav = trav.next
        
        return False            

    def index_by_val(self, val):
        trav = self.head
        idx = 0

        while trav != None:
            if trav.data == val:
                return idx

            trav = trav.next
            idx += 1
        
        return -1      

    def contains(self, val):
        return self.index_by_val(val) != -1

if __name__=="__main__":

    dll = DoublyLinkedList()

    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.add(4)

    print(dll)

    assert dll.contains(3) == True
    
    assert dll.contains(10) == False

    dll.remove_by_index(2)

    print(dll)
