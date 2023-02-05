class Set:
    def __init__(self, *initElement) -> None:
        self._element = list(initElement)

    def __len__(self):
        return len(self._element)
    
    def __contains__(self, item):
        return item in self._element
    
    def add(self, item):
        assert item not in self._element, "Item cant be duplicate in set"
        self._element.append(item)

    def remove(self, item):
        assert item  in self._element, "Item not in set"
        self._element.remove(item)

    def printSet(self):
        for i in range(len(self._element)):
            print(self._element[i])
    
    # Extra functions
    def __eq__(self, setB):
        return len(self._element) == len(setB._element)
    
    def subSet(self, setB):
        for i in self._element:
            if i not in setB._element:
                return False
            
    def union(self, setB):
        newSet=Set()
        for i in self._element:
            newSet.add(i)
        for element in setB._element:
          if element not in newSet._element:
            newSet._element.append(element)
        newSet.printSet()

    def intersection(self, setB):
        newSet = Set()
        for i in self._element:
            newSet.add(i)
        for element in self._element:
            if element not in setB._element:
                newSet.remove(element)
        newSet.printSet()

    def difference(self, setB):
        newSet=Set()
        newSet._element = self._element
        for element in setB._element:
          if element in newSet._element:
            while element in newSet._element:
                newSet._element.remove(element)
        newSet.printSet()

    def properSubset(self, setB):
        if len(setB._element) == len(self._element): return False
        return self.subSet(setB)
   

setA = Set(1, 2, 3, 4, 5)
setB = Set(4, 5, 6, 7, 8)

print("Length of setA:", len(setA))
print("Length of setB:", len(setB))

print("Is 3 in setA:", 3 in setA)
print("Is 3 in setB:", 3 in setB)

setA.add(6)
setA.remove(1)
setB.add(1)
setB.remove(6)
print("Set A:")
setA.printSet()
print("Set B:")
setB.printSet()

print("Are setA and setB equal:", setA == setB)

print("Is setA a subset of setB:", setA.subSet(setB))

print("Union of setA and setB:")
setA.union(setB)

print("Intersection of setA and setB:")
setA.intersection(setB)

print("Difference of setA and setB:")
setA.difference(setB)

print("Is setA a proper subset of setB:", setA.properSubset(setB))