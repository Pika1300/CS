'''your bst here'''
class BST:
    class Node:
        def __init__ (self, value = None):
            #print("s-node")
            
            self.value = value
            self.amount = 1
            self.left=None
            self.right=None
            #print(self.value)
            #print("e-node")
            
            
    def __init__(self) -> None:
        self.sizz=0
        self.tip=None
        self.heigh=-1
    def createTree(self,node):
        self.tip=node
        self.sizz+=1
        self.heigh=0


    def attach_l(self,item,node):
        self.sizz+=1
        print(item)
        node.left=self.Node(item)

    def attach_r(self,item,node):
        self.sizz+=1
        print(item)
        node.right=self.Node(item)

    def traverse_attach(self,item,node):
        
        if self.ht>self.heigh:
            self.heigh=self.ht
        self.ht+=1
        if item==node.value:
            node.value.count+=1
        elif item<node.value:
            if node.left==None:
                self.attach_l(item,node)
            else:
                self.traverse_attach(item,node.left)
        elif item>node.value:
            if node.right==None:
                self.attach_r(item,node)
            else:
                self.traverse_attach(item,node.right)
    def traverse_find(self,item,node):
        if node==None:
            return None
        elif item==node.value:
            return(node.value.count)
        elif item<node.value:
            return(self.traverse_find(item,node.left))
        elif item>node.value:
            return(self.traverse_find(item,node.right))
    def traverse(self,node):
        #print("T"+str(node.value))
        if node.left!=None:
            self.traverse(node.left)
            self.inord.append(node.value)
        if node.right!=None:
            if node.left==None:
                self.inord.append(node.value)
            self.traverse(node.right)
        if node.right==None and node.left==None:
            self.inord.append(node.value)
            
    def pretraverse(self,node):
        #print("T"+str(node.value))
        self.inord.append(node.value)
        if node.left!=None:
            self.pretraverse(node.left)
        if node.right!=None:
            self.pretraverse(node.right)
                   
        
    def posttraverse(self,node):
        #print("T"+str(node.value))
        if node.left!=None:
            self.posttraverse(node.left)
        if node.right!=None:
            self.posttraverse(node.right)
        self.inord.append(node.value)


    def add(self,item):
        if self.tip==None:
            print(item)
            self.createTree(self.Node(item))      
        else:
            
            self.ht=0
            self.traverse_attach(item,self.tip)
        return(self)

    def size(self):
        print(self.sizz)
        return(self.sizz) 
     
    def is_empty(self):
        if self.tip==None:
            return True
        else:
            return False
        
    def height(self):
        print(self.heigh)
        return self.heigh 
    
    def find_successor(self,node):
        if node.left==None:
            self.remove(node)
            return(node)
        else:
            return(self.find_successor(node.left))
    def reml(self,pnode):
        node=pnode.left
        if node.left==None and node.right==None:
            pnode.left=None
            self.heigh-=1
        elif node.left!=None or node.right!=None:
            if node.right==None:
                pnode.left=node.left
            elif node.left==None:
                pnode.left=node.right
        elif node.left!=None and node.right!=None:
            pnode.left=self.find_successor(node)
            pnode.left.left=node.left
            pnode.left.right=node.right
    def remr(self,pnode):
        node=pnode.right
        if node.left==None and node.right==None:
            pnode.right=None
            self.heigh-=1
        elif node.left!=None or node.right!=None:
            if node.right==None:
                pnode.right=node.left
            elif node.left==None:
                pnode.right=node.right
        elif node.left!=None and node.right!=None:
            pnode.right=self.find_successor(node)
            pnode.right.left=node.left
            pnode.right.right=node.right
    def traverse_remove(self,item,node):
        if item==node.left.value:
            self.reml(node)
        elif item==node.right.value:
            self.remr(node)
        else:
            if item<node.value:
                self.traverse_remove(item,node.left)
            elif item>node.value:
                self.traverse_remove(item,node.right)
    def remove(self,item):
        self.sizz-=1
        if self.traverse_find(item,self.tip)!=None:
            self.traverse_remove(item,self.tip)
        return(self)

    def find(self,item):
        amount=self.traverse_find(item,self.tip)
        if amount== None:
            raise ValueError("No Item Found")
        else:
            print(amount)
            return amount
            

    def inorder(self):
        self.inord=[]
        self.traverse(self.tip)
        print(self.inord)
        print(len(self.inord))
        return self.inord
    def preorder(self):
        self.inord=[]
        self.pretraverse(self.tip)
        print(self.inord)
        print(len(self.inord))
        return self.inord
    def postorder(self):
        self.inord=[]
        self.posttraverse(self.tip)   
        print(self.inord)
        print(len(self.inord))
        return self.inord 

