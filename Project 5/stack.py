class Stack:
    class SListNode:
        def __init__ (self, item):
            self.value = item
            self.next = None
            self.back=None
    def __init__(self):
        self.siz=0
        self.head=self.SListNode(None)
        self.tail=self.SListNode(None)
        self.head.next=self.tail
        self.tail.back=self.head

    def push(self, item):
        self.siz+=1
        #print("push")
        #print(item)
        if self.head.next==self.tail:
            self.topp=self.SListNode(item)
            self.head.next=self.topp
            self.tail.back=self.topp
            self.topp.back=self.head
            self.topp.next=self.tail
        else:
            self.topp.next=self.SListNode(item)
            self.topp.next.back=self.topp
            self.topp=self.topp.next
            self.topp.next=self.tail
            self.tail.back=self.topp
        #print(self)

            
    def pop(self):
        #print("pop")
        if self.tail.back==self.head:
            raise IndexError("Zero items")
        else:
            self.siz-=1
            ret=self.topp
            self.topp=self.topp.back
            self.topp.next=self.tail
            self.tail.back=self.topp
            #print(ret.value)
            #print(self)
            return(ret.value)
            
        
    def top(self):
        if self.tail.back==self.head:
            raise IndexError("Zero items")
        else:
            return(self.topp.value)
    
    def size(self):
        return(self.siz)
    
    def clear(self):
        #print(self)
        #print("c")
        self.siz=0
        self.head=self.SListNode(None)
        self.tail=self.SListNode(None)
        self.head.next=self.tail
        self.tail.back=self.head
    def __str__(self):
        node=self.head
        l=""
        if node.next==self.tail:
            return("There is no list.")
        else:
            node=node.next
            while node.next!=None:
                l+=","+str(node.value)
                node=node.next
            
            return(l)
            
from random import randint
s=Stack()
for x in range(10):
    n=randint(0,9)
    print(n)
    s.push(n)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
s.push(2)
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)