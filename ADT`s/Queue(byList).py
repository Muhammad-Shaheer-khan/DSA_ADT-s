# Using List
class Queue:
    def __init__(self) -> None:
        self._elements = list()

    def __len__(self):
        return len(self._elements)
    
    def isEmpty(self):
        return len(self._elements) == 0
    
    def enqueue(self, item):
        self._elements.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._elements.pop(0)
    
    def head(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._elements[0]
    
    def tail(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._elements[-1]
    
    def printQueue(self):
        assert not self.isEmpty(), "Queue is empty"
        for i in self._elements:
            print(i)


q = Queue()
print("Is Queue empty:\t",q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("Lenght of Queue (After enqueue):",len(q))
print("Is Queue empty:\t",q.isEmpty())
print("Queue items:")
q.printQueue()
print()
print("Dequeue:",q.dequeue())
print("Head:",q.head())
print("Tail:",q.tail())
print()
print("Queue items:")
q.printQueue()
print("Dequeue:",q.dequeue())
print("Head:",q.head())
print("Tail:",q.tail())
