class listNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        newNode = listNode(data)
        if self.head == None:
            self.head = newNode
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = newNode

    def prepend(self, data):
        newNode = listNode(data)
        newNode.next = self.head
        self.head = newNode

    # def delete_node(self, key):
    #     cur_node = self.head
    #     if cur_node and cur_node.data == key:
    #         self.head = cur_node.next
    #         cur_node = None
    #         return
    #     prev = None
    #     while cur_node and cur_node.data != key:
    #         prev = cur_node
    #         cur_node = cur_node.next
    #     if cur_node is None:
    #         return
    #     prev.next = cur_node.next
    #     cur_node = None
    def delete_value(self, data):
        # cur_node = self.head
        if self.head.data == data:
            self.head = self.head.next
            return
        cur_node = self.head
        prev = None
        while cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next
            if cur_node == None:
                return "Value not found"
        prev.next = cur_node.next
    
    def print_LinkedList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next