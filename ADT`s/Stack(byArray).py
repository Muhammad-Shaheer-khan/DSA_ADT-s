from Array import Array

# By Array
class Stack:
    def __init__(self, size) -> None:
        self.size = size
        self._elements = Array(self.size)

    def maxLen(self):
        return self.size
    
    def len(self):
        valCount = 0
        for i in (self._elements):
            if i != None:
                valCount += 1
            else: 
                return valCount
        return valCount
    
    def isEmpty(self):
        if self._elements[0] == None:
                return True
        return False

    def push(self, item):
        
        assert self.len() != self.maxLen(), "Stack is full"
        for i in reversed(range(self.len())):
            self._elements[i+1] = self._elements[i]
        self._elements[0] = item

    def pop(self):
        assert not self.isEmpty(), "Stack empty"
        popValue =  self._elements[0]
        for i in range(self.len()):
            self._elements[i] = self._elements[i+1]   
        return popValue
    
    def peek(self):
        return self._elements[0]
    
    # Extra function
    def printValue(self):
        # array = []
        for i in range(len(self._elements)):
            if self._elements[i] != None:
                # array.append() 
                print(self._elements[i])

stack = Stack(5)
print("Is stack empty:", stack.isEmpty())
for i in range(2,5):
    stack.push(i)

print("Is stack empty:", stack.isEmpty())
print(f"Lenght: {stack.len()}")
print(f"Max Lenght: {stack.maxLen()}")
print("Stack is lool like:")
stack.printValue()
print("Peek of stack:", stack.peek())
print("Pop value:",stack.pop())
print("Peek of stack:", stack.peek())
