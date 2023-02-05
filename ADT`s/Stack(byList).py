# By List
class Stack:
    def __init__(self) -> None:
        self._elements = list()

    def __len__(self):
        return len(self._elements)
    
    def isEmpty(self):
        return len(self._elements) is 0
    
    def push(self, item):
        self._elements.insert(0, item)

    def pop(self):
        assert not self.isEmpty(), "Stack empty"
        return self._elements.pop(0)
    
    def peek(self):
        return self._elements[0]

    def printValues(self):
        for i in range(len(self._elements)):
            print(self._elements[i])


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