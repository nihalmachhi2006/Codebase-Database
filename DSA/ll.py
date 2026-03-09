class Node:
    def __init__(self,info,next = None):
        self.data = info
        self.next = next

class linkedlist:
    def __init__(self,head = None):
        self.head = head

    def insertedatstart(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def removenode(self,value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next = None

    def insertedatmiddle(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def insertedatend(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printll(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = linkedlist()
obj.insertedatend(10)
obj.insertedatend(20)
obj.insertedatend(30)
obj.insertedatstart(5)
obj.insertedatmiddle(40,20)
obj.removenode(30)
obj.printll()

