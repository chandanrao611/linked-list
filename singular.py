# create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

##
# firstNode = Node('Chandrakesha')
linkedList = LinkedList()
# linkedList.insert(firstNode)
linkedList.printList()