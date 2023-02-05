from ctypes import py_object as empty_places

class Array:
    def __init__(self, size) -> None:
        self.size = size
        self.array = (empty_places*self.size)()
        self.clear(None)

    def clear(self, value):
        for i in range(len(self.array)):
            self.array[i] = value

    def __len__(self):
        return len(self.array)

    def remove(self, ndx):
        assert ndx != None, "Index value is none"
        temp = self.array[ndx] 
        self.array[ndx] = None
        return temp

    def __setitem__(self, ndx, item):
        assert  ndx < self.size, "Array out of range"
        self.array[ndx] = item

    def __getitem__(self, ndx):
        assert ndx < self.size, "Array out of range"
        return self.array[ndx]
    
class Queue:
    def __init__(self, size) -> None:
        self.size = size
        self._element = Array(self.size)

    def maxLen(self):
        return self.size 
    
    def len(self):
        count = 0
        for i in range(len(self._element)):
            if self._element[i] != None :
                count +=1  
        return count
    
    def isEmpty(self):
        return self.len() == 0
    
    def enqueue(self, item):
        assert self.len() != self.size, "Queue overflow"
        lenght = self.len()
        if lenght == 0:
            self._element[0] = item
            return
        self._element[lenght] = item

    def dequeue(self):
        for i in range(len(self._element)):
            if self._element[i] != None:
                return self._element.remove(i)  
    
    def head(self):
        for i in range(len(self._element)):
            if self._element[i] is not None:   
                return self._element[i]
        
    def tail(self):
        for i in reversed(range(len(self._element))):
            if self._element[i] is not None:   
                return self._element[i]
        
    def printQueue(self):
        for i in range(len(self._element)):
            if self._element[i] is not None:
                print(self._element[i])

q = Queue(5)
print("Is Queue empty:\t",q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("Lenght of Queue (After enqueue):",q.len())
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
