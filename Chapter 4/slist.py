from random import randint
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
                return
            head=self._head.value
            while comp!=self._head:
                #find location
                while n.value==next.value:
                    comp=next
                    next=comp.next
                    if next==None:
                        break
                if comp.next==None:
                    comp.next=n
                    n.next=None
                    self._head=n
                    break
                elif comp.value<=n.value and next.value >= n.value:
                    comp.next=n
                    n.next=next
                    break
                #append at the end
                #go to next node
                else:
                    comp=next
                    next=comp.next
                
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        comp=self._tail
        if comp==None:
            return None
        next=comp.next
        while True:
            if comp.value==value:
                return (comp.value)
            elif comp.next==None:
                break
            else:
                comp=next
                next=comp.next
                
        return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        comp=self._tail
        if comp==None:
            return False
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
        if comp==None:
            return
        next=comp.next
        found=False
        #checkstail
        if comp.value==value:
            while comp.value==value:
                self._size-=1
                self._tail=next
                comp=self._tail
                if comp==None:
                    self._head=None
                    break
                next=comp.next
                
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

    '''Return size of the list'''
    def size(self):
        return (self._size)

    '''Return an iterator for the list'''
    def __iter__(self):
        self.it=self._tail
        return self

    def __next__(self):
        val=self.it
        if val==None:
            raise StopIteration("List out of Bounds.")
        self.it=val.next
        return val.value
    
    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        if index>(self._size-1) or self._size==0:
            raise Exception
        else:
            comp=self._tail
            next=comp.next
            for x in range(index):
                comp=next
                next=comp.next
            return comp.value

    def __len__(self):
        return self._size

    
lyst=SList()

for x in range(10):
    val = randint(1,200)
    #print(val)
    lyst.insert(val)
    #print(lyst)
for z in range(10):
    val = randint(0,10)
    #print(val)
    #lyst.remove_all(val)
print(lyst)
print(lyst.__getitem__(0))
