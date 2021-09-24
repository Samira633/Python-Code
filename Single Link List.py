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

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def addIn(self,data, prenode):
        new_node=Node(data)
        if not prenode:
            print("this node does not exist")
            return
        new_node.next=prenode.next
        prenode.next=new_node
    def deleteNode(self,data):
        cur_node=self.head
        if cur_node and cur_node.data==data:
            self.head=cur_node.next
            cur_node=None
            return
        pre=None
        while cur_node and cur_node.data!=data:
            pre=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            return
        pre.next=cur_node.next
        cur_node=None

    def delete_node_a_pos(self,pos):
        cur_node=self.head
        if pos==0:
            self.head=cur_node.next
            cur_node=None
            return

        if pos==1:
            second_node=cur_node.next
            self.head.next=second_node.next
            second_node=None
            return
        pre=None
        count=2

        while cur_node and pos!=count:
            pre=cur_node
            cur_node=cur_node.next
            count+=1

        if cur_node is None:
            return

        pre.next=cur_node.next
        cur_node=None







linklinst=LinkedList()
linklinst.append("A")
linklinst.append("B")
linklinst.prepend("c")
linklinst.addIn("E",linklinst.head.next)
linklinst.printlinkedlist()
#linklinst.deleteNode("E")
linklinst.delete_node_a_pos(3)
linklinst.printlinkedlist()