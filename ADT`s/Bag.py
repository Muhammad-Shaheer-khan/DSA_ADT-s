import random
class bag:

    def __init__(self) -> None:
        self.bagItem = list()

    def addItem(self, item):
        self.bagItem.append(item)

    def showItem(self):
        print("Bag items are:")
        c = 1
        for i in self.bagItem:
            print(str(c)+".", i)
            c+=1

    def __contains__(self,item):
        return item in self.bagItem
    def __len__(self):
        return len(self.bagItem)
    
    def removeItem(self):
        self.RandomItem = random.choice(self.bagItem)
        self.bagItem.remove(self.RandomItem)
        print("Random item is pop out from your bag:\t", self.RandomItem)

bagObj = bag()
bagObj.addItem("book")
bagObj.addItem("pen")
bagObj.addItem("pencil")
bagObj.addItem("eraser")

bagObj.showItem()
print("Book is in bag:\t","book" in bagObj)

print("Number of items in the bag:", len(bagObj))

bagObj.removeItem()

bagObj.showItem()