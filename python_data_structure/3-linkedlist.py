class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)
    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item does not exist in linked list")
    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

linkedlist = LinkedList(3)
linkedlist.printlist() # 3
linkedlist.add(4)
linkedlist.printlist() # 3 4