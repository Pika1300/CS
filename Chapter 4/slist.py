
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._tail=None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        n=self.SListNode(value)
        #print(n)
        if self._head==None:
            self._head=n
            self._tail=n
            self._size+=1
        elif n.value>self._head.value:
            self._head.next=n
            self._head=n
            self._size+=1
        elif n.value<self._tail.value:
            n.next=self._tail
            self._tail=n
            self._size+=1
        #if not less than tail or greater than tail
        else:
            self._size+=1
            comp=self._tail
            next=comp.next
            #if only one node
            if next==None:
                comp.next=n
                self._head=n
            while comp!=self._head:
                #find location
                while n.value==next.value:
                    comp=next
                    next=comp.next
                    if next==None:
                        break
                if comp.value<n.value and next.value >= n.value:
                    comp.next=n
                    n.next=next
                    break
                #append at the end
                elif comp.next==None:
                    comp.next=n
                    n.next=None
                    self._head=n
                    break
                #go to next node
                else:
                    comp=next
                    next=comp.next
                
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        pass

    '''Remove the first occurance of value.'''
    def remove(self, value):
        comp=self._tail
        next=comp.next
        found=False
        #checkstail
        if comp.value==value:
            self._tail=next
            found=True
            self._size-=1
            return found
        #iterates
        while next!=None:
            if next.value==value:
                comp.next=next.next
                found=True
                self._size-=1
                break
            else:
                comp=next
                next=comp.next
        return found

    '''Remove all instances of value'''
    def remove_all(self, value):
        comp=self._tail
        next=comp.next
        found=False
        #checkstail
        if comp.value==value:
            while comp.value==value:
                self._tail=next
                comp=self._tail
                next=comp.next
                self._size-=1
            return

        #iterates
        while next!=None:
            if next.value==value:
                comp.next=next.next
                next=comp.next
                self._size-=1
            else:
                comp=next
                next=comp.next

    '''Convert the list to a string and return it'''
    def __str__(self):
        n=self._tail
        #print("Size"+str(self._size))
        l="["
        if n==None:
            return("There is no list.")
        l=l+str(n.value)+""
        n=n.next
        while n!=None:
            l=l+","+str(n.value)
            n=n.next
        l=l+"]"
        return l

    '''Return an iterator for the list'''
    def __iter__(self):
        pass

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        pass

    def __len__(self):
        return self._size

    
lyst=SList()
lyst.insert(5)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(6)
lyst.insert(7)
lyst.insert(8)
lyst.insert(9)
lyst.insert(10)
lyst.insert(11)
lyst.insert(12)
lyst.insert(113)
print(lyst)
lyst.remove_all(6)
print(len(lyst))



print(lyst)
