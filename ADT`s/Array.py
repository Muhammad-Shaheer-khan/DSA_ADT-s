from ctypes import py_object as space

class Array:
    def __init__(self, size) -> None:
        self.size = size
        self._Array = (space*self.size)()
        self.clear(None)

    def clear(self, value):
        for i in range(len(self._Array)):
            self._Array[i]=value 

    def __len__(self):
        return self.size
    
    def remove(self, index):
        assert  self._Array[index] != None, "Index is None"
        temp = self._Array[index]
        self._Array[index] = None
        if __name__ != '__main__':
            return temp

    def __setitem__(self, index , value):
        assert index >= 0 and index < self.size, "Out of range" 
        self._Array[index] = value

    def __getitem__(self, index):
        assert index >= 0 and index < self.size, "Index not in range"
        return self._Array[index]
    
    # Extra function
    def printValue(self):
        for i in self._Array:
            if i != None:
                print(i) 
    
if __name__ == "__main":
    obj = Array(3)
    print(f"Lenght of an Array {len(obj)}")
    obj[0]='a'
    obj[1]='b'
    obj[2]='c'
    print(f"Lenght of an Array {len(obj)}")
    print("\nArray elements:")
    obj.printValue()
    obj.remove(1)
    print("\nArray elements(After removing index 1):")
    obj.printValue()
    