class _PriorityQEntry ( object ) :
    def __init__ ( self , item , priority ) :
        self . item = item
        self . priority = priority

# Unbounded Priority Queue ADT using list
class PriorityQueue :
    def __init__ ( self ) :
        self . _qList = list ()
    def isEmpty ( self ) :
        return len( self ) == 0
    def __len__ ( self ) :
        return len( self . _qList )

    def enqueue ( self , item , priority ) :
        entry =_PriorityQEntry ( item , priority )
        self . _qList . append ( entry )

    def dequeue ( self ) :
        assert not self . isEmpty () , " Empty queue "
        index = 0
        highest = self._qList[index].priority
        for i in range (len( self._qList )) :
            if self . _qList [ i ]. priority > highest :
                highest = self . _qList [ i ]. priority
                index = i
        entry = self . _qList . pop ( index )
        return entry . item
    
q =  PriorityQueue()
print("Lenght:\t",len(q))
print("Is Queue empty:",q.isEmpty())
item = 4
for priority in range(item):
    q.enqueue(item, priority)
    print(f"Enqueue {item}, Priority {priority}")
    item -= 1

print("Dequeue: ",q.dequeue())
print("Enqueue another value:")
item = 55
priority = 1
q.enqueue(item, priority)
print(f"Enqueue {item}, Priority {priority}")
print()
print("Again dequeuing",q.dequeue())

