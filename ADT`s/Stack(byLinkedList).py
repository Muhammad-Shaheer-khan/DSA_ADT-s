# By Linked list
class newItem:
    def __init__(self, item, link) -> None:
        self.item = item
        self.next = link

class Stack:
    def __init__(self) -> None:
        self._top = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self._top is None
    
    def push(self, item):
        self._top = newItem(item, self._top)
        self.size += 1

    def pop(self):
        assert not self.isEmpty(), "Stack empty"
        node = self._top
        self._top = self._top.next
        self.size -= 1
        return node.item
    
    def peek(self):
        assert not self.isEmpty(), "Stack empty"
        return self._top.item
    
    def printValues(self):
        temp = self._top
        while temp.next:
            print(temp.item)
            temp = temp.next
        print(temp.item)
            

stack = Stack()
print("Is stack empty:", stack.isEmpty())
for i in range(2,5):
    stack.push(i)

print("Is stack empty:", stack.isEmpty())
print(f"Lenght: {len(stack)}")
print("Stack is lool like:")
stack.printValues()
print("Peek of stack:", stack.peek())
print("Pop value:",stack.pop())
print("Peek of stack:", stack.peek())