class mapEntry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class map:
    def __init__(self) -> None:
        self.dict = list()

    def __len__(self):
        return len(self.dict)
    
    def __contains__(self, key):
        return ((self._findPosition(key)) is not None)
    
    def _findPosition(self, key):
        for i in range(len(self.dict)):
            if self.dict[i].key == key:
                return i
        return None
    
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx != None:
            self.dict[ndx].value = value

        else:
            newEntry = mapEntry(key, value)
            self.dict.append(newEntry)

    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "key doesn`t exists"
        return self.dict[ndx].value

myMap = map()
myMap.add("Name", "John")
myMap.add("Age", 30)
myMap.add("Occupation", "Developer")
print("Length of the map:", len(myMap))
if "Name" in myMap:
    print("Key 'Name' exists")
print("Value of key 'Name':", myMap.valueOf("Name"))

myMap.add("Name", "Jane")
print("Value of key 'Name' after update:", myMap.valueOf("Name"))
