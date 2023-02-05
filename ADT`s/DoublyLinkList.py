class LinkListNode:
    def __init__(self, item) -> None:
        self.previous = None
        self.item = item
        self.next = None

class DoublyLinkeList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.head is None
    
    def add_front(self, item):
        newNode = LinkListNode(item)
        if self.isEmpty():
            self.size += 1
            self.head = newNode
            return
        newNode.next = self.head
        self.head.previous = newNode
        self.size += 1
        self.head = newNode
        return
    
    def remove_front(self):
        assert not self.isEmpty(), "Queue is empty"
        self.head = self.head.next
        self.size -= 1
        self.head.previous = None

    def add_rear(self, item):
        newNode = LinkListNode(item)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        self.size += 1
        newNode.previous = temp

    def remove_rear(self):
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.size -= 1
        prev.next = None

    def printValues(self):
        temp = self.head
        while temp.next:
            print("Current:",temp.item)
            print("Previous:",temp.previous)
            print("Next:",temp.next)
            temp = temp.next
        print("Current:",temp.item)
        print("Previous:",temp.previous)
        print("Next:",temp.next)

o = DoublyLinkeList()
o.add_front(2)
# o.printValues()
print()
o.add_front(5)
o.add_front(6)
o.add_front(7)
# o.printValues()
print()
o.remove_front()
# o.printValues()
o.remove_rear()
print()
o.printValues()
o.add_rear(50)
print()
o.printValues()