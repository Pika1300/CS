'''your bst here'''
class BST:
    class Node:
        def __init__ (self, value = None):
            print("s-node")
            
            self.value = value
            self.amount = 1
            self.left=None
            self.right=None
            print(self.value)
            print("e-node")
    def __init__(self) -> None:
        self.sizz=0
        self.tip=None
        self.heigh=0
    def createTree(self,node):
        self.tip=node
        self.sizz+=1


    def attach_l(self,item,node):
        node.left=self.Node(item)

    def attach_r(self,item,node):
        node.right=self.Node(item)

    def traverse(self,item,node):
        if item==node.value:
            
            node.amount+=1
        elif item<node.value:
            if node.left==None:
                self.attach_l(item,node)
            else:
                self.traverse(item,node.left)
        elif item>node.value:
            if node.right==None:
                self.attach_r(item,node)
            else:
                self.traverse(item,node.right)
        
    def add(self,item):
        if self.tip==None:
            self.createTree(self.Node(item))      
        else:
            self.sizz+=1
            self.traverse(item,self.tip)
            


    def size(self):
        return(self.sizz)  
    def is_empty(self):
        if self.tip==None:
            return True
        else:
            return False
        
    def height():
        pass  
    def remove():
        pass  
    def find():
        pass  
    def inorder():
        pass  
    def preorder():
        pass
    def postorder():
        pass    

    pass
from random import randint

lst=BST()
lst.add(3)
lst.add(2)
for x in range(100):
    lst.add(randint(1,5))
print(lst.size())