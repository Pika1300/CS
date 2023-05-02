import math
class Graph:

    class Node:
        def __init__(self,label) -> None:
            self.label=label
            self.connections=[]#(dest,weight)

        def pc(self):
            print(self.connections)
    def __init__(self) -> None:
        self.vertices=[]#node
    def __str__(self) -> str:
        
        returnstatement='digraph G {\n'
        for x in self.vertices:
            for y in x.connections:
                returnstatement+= f"   {x.label} -> {y[0]} [label=\"{float(y[1])}\",weight=\"{float(y[1])}\"];\n"
        return returnstatement+"}"

    def find_node(self,label)-> Node:
        for x in self.vertices:
            if x.label == label:
                return x
        return None
    def find_edge(self,snode,dnode)-> tuple:
        for edge in snode.connections:
            if edge[0]==dnode.label:
                return edge
        else:
            return None


    def add_vertex(self,label):
        
        if self.find_node(label)==None:
            self.vertices.append(self.Node(label))
        else:
            raise ValueError("Node already in graph")
        if isinstance(label,str)==False:
            raise ValueError("Not String")
        return self

    def add_edge(self,src,dest,w):
        print(src)
        print(dest)
        print(w)
        print()
        if isinstance(w,int)==True or isinstance(w,float)==True:
            pass
        else:
            raise ValueError("Not int")

        if isinstance(src,str)==False:
            raise ValueError("Not str")
        if isinstance(dest,str)==False:
            raise ValueError("Not str")
        snode=self.find_node(src)
        dnode=self.find_node(dest)
        if snode !=None and dnode!=None:
            if self.find_edge(snode,dnode)==None:
                snode.connections.append((dest,w))
                
            else:
                raise ValueError("Edge already added")
        else:
            raise ValueError("Nodes not added")
        return self

  
    def get_weight(self,src,dest):
        print(src)
        print(dest)
        snode=self.find_node(src)
        dnode=self.find_node(dest)
        if snode==None:
            raise ValueError("Node not added")
        if dnode==None:
            raise ValueError("Node not added")
        edge=self.find_edge(snode,dnode)
        if edge==None:
            return math.inf
        return (edge[1])
    

    def dfscheck_complete(self,clist,label):
        if clist==[]:
            return False
        else:
            for x in clist:
                if x==label:
                    return True
            return False
        

    def dfs(self,starting_vertex)->iter:
        vertices=self.vertices
        cur_vertex=starting_vertex
        nodeconnections=[starting_vertex] 
        completed=[starting_vertex] 
        yield cur_vertex      
        for p in range(len(vertices)-1):   

            ##############  
            
            for x in vertices:
                if x.label==cur_vertex:
                    curnode=x   
            t=[]
            for x in curnode.connections:
                label=x[0]
                t.append(label)
            t.sort()
            t.reverse()
            ############## 
            for x in t:
                if self.check_complete(completed,x)==False:
                    completed.append(x)
                    nodeconnections.insert(0,x)
                else:
                    for y in nodeconnections:
                        if y==x:
                            nodeconnections.remove(x)
                            nodeconnections.insert(0,x)
            
            cur_vertex=nodeconnections[0]
            nodeconnections.pop(0)
            yield cur_vertex

    def check_complete(self,clist,label):
        if clist==[]:
            return False
        else:
            for x in clist:
                if x==label:
                    return True
            return False
    def bfs(self,starting_vertex)->iter:
        print(self)
        print(starting_vertex)
        vertices=self.vertices
        cur_vertex=starting_vertex
        nodeconnections=[starting_vertex] 
        completed=[starting_vertex] 
        yield starting_vertex       
        while nodeconnections!=[]:
            nodeconnections.pop(0)     
            for x in vertices:
                if x.label==cur_vertex:
                    curnode=x   
            t=[]
            for x in curnode.connections:
                label=x[0]
                t.append(label)
            t.sort()
            for x in t:
                if self.check_complete(completed,x)==False:
                    yield x
                    completed.append(x)
                    nodeconnections.append(x)
            if nodeconnections!=[]:   
                cur_vertex=nodeconnections[0]
            
            #print(nodeconnections)
        
        
        
    def dsp_helper(self,dicti,label):
        
        if dicti[label][0]==0:
            return label
        else:
            return (label+self.dsp_helper(dicti,dicti[label][1]))
    def dsp(self,src,dest) ->tuple:
        visited=[]
        univisted=[]
        weights={}
        for x in self.vertices:
            univisted.append(x.label)
            weights.update({x.label:(None,None)})
        weights.update({src:(0,"")})
        low_label=''
        lowest_num=100000000000
        while univisted!=[]:
            lowest_num=100000000000
            
            for k,v in weights.items():
                if v[0]==None:
                    pass
                else: 
                    for l in univisted: 
                        if k==l:
                            if v[0]<lowest_num:
                                lowest_num=v[0]
                                low_label=k
            curnode=self.find_node(low_label)
            visited.append(low_label)
            univisted.remove(low_label)
            for x in curnode.connections:
                for u in univisted:
                    if u==x[0]:
                        linew=weights[curnode.label][0]
                        
                        if linew==None:
                            linew=0
                        #print("w"+str(linew))
                        linea=x[1]

                        #print("a"+str(linea))
                        weights.update({x[0]:(linew+linea,curnode.label)})
        li=str(self.dsp_helper(weights,dest))[::-1]
        oi=[]
        for x in li:
            oi.append(x)
        return ((weights[dest][0]),oi)
            
            

    def dspall_helper(self,weights,src):

        a=weights[src]
        if a[1]=='':
            return 0
        else:
            num= a[0]+(weights[a[1]][0])
            
            return num
    def dsp_all(self,src):
        visited=[]
        univisted=[]
        weights={}
        for x in self.vertices:
            univisted.append(x.label)
            weights.update({x.label:(None,[None])})
        weights.update({src:(0,"")})
        low_label=''
        lowest_num=100000000000
        while univisted!=[]:
            lowest_num=100000000000
            
            for k,v in weights.items():
                if v[0]==None:
                    pass
                else: 
                    for l in univisted: 
                        if k==l:
                            if v[0]<lowest_num:
                                lowest_num=v[0]
                                low_label=k
            curnode=self.find_node(low_label)
            visited.append(low_label)
            univisted.remove(low_label)
            for x in curnode.connections:
                for u in univisted:
                    if u==x[0]:
                        linew=weights[curnode.label][0]
                        if linew==None:
                            linew=0
                        else:
                            weights.update({x[0]:(0,curnode.label)})
                            linew= (self.dspall_helper(weights,x[0]))
                            
                        #print("w"+str(linew))
                        linea=x[1]
                        #print("a"+str(linea))
                        
                        weights.update({x[0]:(linew+linea,curnode.label)})
        weights2={}
        for r in self.vertices:
            path=str(self.dsp_helper(weights,r.label))[::-1]
            plist=[]
            for w in path:
                plist.append(w)
            weights2.update({r.label:plist}) 
        return weights2     
    def show(self,weights2):
        for e,r in weights2.items():
            yield "{"+str(e)+": "+str(r)+"}"
            
    

g=Graph()
vertexes=["A","B","C","D","E","F"]
connections=[("A","B",2),("A","F",9),("B","C",8),("B","D",15),("B","F",6),("C","D",1),("E","D",3),("E","C",7),("F","B",6),("F","E",3),]
for x in vertexes:
    g.add_vertex(x)

for x in connections:
    g.add_edge(x[0],x[1],x[2])

def main():
    print(g)
    print("Starting BFS with vertex A")
    for vertex in g.bfs("A"):
        print(vertex, end = "")

    print()
    print("starting DFS with vertex A")
    for vertex in g.dfs("A"):
        print(vertex, end = "")
    print()
    print(g.dsp("A","F"))
    s=g.show(g.dsp_all("A"))
    for x in s:
        print(x)
if __name__ == "__main__":
    main()



