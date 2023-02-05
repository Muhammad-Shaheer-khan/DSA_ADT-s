# Using LinkList

class newNode:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def isEmpyt(self):
        return self.front is None
    
    def enqueue(self, item):
        newnode = newNode(item) 
        if self.isEmpyt():
            self.size += 1
            self.front = self.rear = newnode
            self.rear.next = self.front
            return
        temp = self.front
        while temp.next.item != self.front.item:
            temp = temp.next
        self.size += 1
        self.rear = temp.next = newnode
        self.rear.next = newnode.next = self.front

    def dequeue(self):
        assert not self.isEmpyt(), "Queue is empty"
        self.size -= 1
        if len(self) == 1:
            self.front = None
            self.rear = None
            return
        temp = self.front
        self.front = temp.next
        self.rear.next = self.front

    def printQueueNode(self):
        ## uncomment this for circular print, for stop the while loop press cntrl+c in terminal
        # temp = self.front
        # while temp.next:
        #     print(temp.item)
        #     temp = temp.next
        print(self.front.item, self.front.next.item, self.front.next.next.item, self.front.next.next.next.item, self.front.next.next.next.next.item )
    
    def printQueueNode01(self):
        temp = self.front
        count = 0
        while temp.next and count <= 20 :
            count += 1
            print(temp.item)
            temp = temp.next


q = Queue()
print("Lenght:\t", len(q))
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print("Lenght:\t", len(q))
print(f"\nCurrent items in Queue:(Showing in circular foam)")
q.printQueueNode()
q.dequeue()
print("After dequeue: (circular queue)")
q.printQueueNode01()
print("But the lenght is:\t", len(q))
