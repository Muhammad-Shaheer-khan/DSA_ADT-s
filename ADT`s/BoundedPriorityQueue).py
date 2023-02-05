class QueueNode:
    def __init__(self, item, priority) -> None:
        self.item = item
        self.priority = priority
        self.next = None

class Queue:
    def __init__(self, boundary) -> None:
        self._head = None
        self.boundary = boundary
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, item, priority):
        assert self.size != self.boundary, "Queue reaches its limit"
        newItem = QueueNode(item, priority)
        if self.isEmpty() or priority > self._head.priority :
            self.size += 1
            newItem.next = self._head 
            self._head = newItem
            return
        temp = self._head
        while temp.next is not None and temp.next.priority >= newItem.priority :
            temp = temp.next
        self.size += 1
        newItem.next = temp.next
        temp.next = newItem

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        temp = self._head
        self._head = temp.next
        self.size -= 1
    
    def head(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._head.item
    
    def tail(self):
        assert not self.isEmpty(), "Queue is empty"
        temp = self._head
        while temp.next:
            temp = temp.next
        return temp.item

    def printQueue(self):
        temp = self._head
        while temp.next:
            print(temp.item)
            temp = temp.next
        print(temp.item)

q = Queue(3)
print(f"len {len(q)}")
q.enqueue('d', 10)
print(f"len {len(q)}")
q.enqueue('b', 30)
print(f"len {len(q)}")
q.enqueue('c', 20)
print(f"len {len(q)}")

print("Head:\t",q.head())
print("Tails:\t",q.tail())
print("\nThis is not an error")
q.enqueue('a', 60)
print(f"len {len(q)}")


