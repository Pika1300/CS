class HashMap:
    def __init__(self) -> None:
        
        self.sizz=0
        self.lf=0
        self.cap=7
        self.dc=self.getList()
        self.calls=0
        self.hits=0
    def chit(self):
        self.hits+=1
    def fc(self):
        self.calls+=1
    def getList(self):
        dc=[]
        for x in range(self.cap):
            dc.append([])
        return dc
    def resize(self):
        self.cap=self.cap*2
        items=self.items()
        self.dc=self.getList()
        for x in items:
            ts=self.sizz
            self.set(x[0],x[1])
            self.sizz=ts
    def loadFactor(self):
        self.lf=self.sizz/self.cap
        if self.lf>.95:
            self.resize()


    def searchGet(self,key,bucket):
        #print(bucket)
        for item in bucket:
            #print(item)
            if item[0]==key:
                return item[1]
        else:
            return None
    def hash(self,key):
        r=key[0]
        c=key[1]
        hs=(((r^2)*(c^2)))%(self.cap)

        return hs
    def get(self,key):
        #print(key)
        bucknum=self.hash(key)
        bucket=(self.dc[bucknum])
        if bucket==[]:
            raise KeyError
        else:
            searchBuck=self.searchGet(key,bucket)
            if searchBuck!=None:
                return searchBuck
            return "Not found"

    def set(self,key,value):
        #print(key)
        #print(value)
        #print()
        
        self.sizz+=1
        bucknum=self.hash(key)
        bucket=(self.dc[bucknum])
        searchBuck=self.searchGet(key,bucket)
        if searchBuck==None:
            bucket.append((key,value))
        else:
            bucket.remove((key,searchBuck))
            bucket.append((key,value))
        
        self.loadFactor()

    def __str__(self):
        for x in self.dc:
            print(str(x))
            #print()
        return("")
        
    def maplen(self):
        for x in self.dc:
            print(len(x))

    def remove(self,key):
        bucknum=self.hash(key)
        bucket=(self.dc[bucknum])
        if bucket==[]:
            return(None)
        else:
            self.sizz-=1
            for itemn in range(len(bucket)):
                if (bucket[itemn])[0]==key:
                    bucket.pop(itemn)
                    break

            
    def clear(self):
        self.sizz=0
        self.lf=0
        self.cap=7
        self.dc=self.getList()

    def size(self):
        return self.sizz
    def capacity(self):
        return self.cap
    
    def items(self):
        k=[]
        for bucket in self.dc:
            for item in bucket:
                k.append(item)
        return k
    
    def keys(self):
        k=[]
        
        for bucket in self.dc:
            for item in bucket:
                k.append(item[0])
        return k

#r=Row
#c=columnt
#key=(r,c)
#value=weight


