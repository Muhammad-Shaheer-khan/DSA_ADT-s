# By Linked list
class newItem:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class Queue:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self._head is None
    
    def head(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._head.item
    
    def tail(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._tail.item

    def enQueue(self, item):
        newNode = newItem(item)
        self.size += 1
        if self.isEmpty():
            self._head = self._tail = newNode
            return
        self._tail.next = newNode 
        self._tail = self._tail.next
        
    def deQueue(self):
        assert not self.isEmpty(), "Queue is empty"
        dequeueValue = self._head.item
        self._head = self._head.next
        self.size -= 1
        return dequeueValue

    
    def printQueue(self):
        assert not self.isEmpty(), "Queue is empty"
        node = self._head
        print(node.item)
        while node .next:
            node = node.next
            print(node.item)

# o = Queue()
# o.enQueue(1)
# o.enQueue(2)
# o.enQueue(3)
# o.printQueue()
# o.deQueue()
# print()
# o.printQueue()

q = Queue()
print("Is Queue empty:\t",q.isEmpty())
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
print("Lenght of Queue (After enqueue):",len(q))
print("Is Queue empty:\t",q.isEmpty())
print("Queue items:")
q.printQueue()
print()
print("Dequeue:",q.deQueue())
print("Head:",q.head())
print("Tail:",q.tail())
print()
print("Queue items:")
q.printQueue()
print("Dequeue:",q.deQueue())
print("Head:",q.head())
print("Tail:",q.tail())
