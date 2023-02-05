class QueueNode:
    def __init__(self, item, priority) -> None:
        self.item = item
        self.priority = priority
        self.next = None

class Queue:
    def __init__(self) -> None:
        self._head = None
        # self._tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, item, priority):
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

q = Queue()
print(f"Lenght:\t{len(q)}")
q.enqueue('d', 10)
q.enqueue('b', 30)
q.enqueue('c', 20)
q.enqueue('a', 60)
print(f"Lenght:\t{len(q)}")
print("Current Queue:")
q.printQueue()
print()
print('head',q.head())
print('tail',q.tail())
print()
print("Dequeuing...")
q.dequeue()
q.printQueue()
print('head',q.head())
print('tail',q.tail())
