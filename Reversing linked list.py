class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printlinkedlist(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node

    def reverse_linkedlis(self):
        pre=None
        while self.head:
            temp=self.head
            self.head=self.head.next
            temp.next=pre
            pre=temp
        self.head=pre

    def reverse(self):
        pre=None
        cur=self.head
        while cur:
             nxt=cur.next
             cur.next=pre
             pre=cur
             cur=nxt
        self.head=pre













linklinst=LinkedList()
linklinst.append("A")
linklinst.append("B")
linklinst.append("c")
linklinst.printlinkedlist()
#linklinst.reverse()
linklinst.reverse_linkedlis()
linklinst.printlinkedlist()