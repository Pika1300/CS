from math import sqrt

lyst =[0,1,2,3,4]
def jump_search(lyst, target):
    comp=0
    pos=0
    lyst_len=len(lyst)
    step=int(sqrt(lyst_len))
   # #print(target)
    for x in range(int(lyst_len/step)):
        comp+=1
        checknum=(lyst[pos])
        ##print(lyst[-1])
        ##print((lyst_len/step))
        #print("checknum"+str(checknum))
        ##print((lyst[-1]))
        ##print("w: "+str((lyst[-1]-checknum)<step))
        ##print("w: "+str(checknum < target))
        #check if step is the target
        if checknum==target:
            return (True, comp)
        
        #checks to see if the target is greater than the number checked
        elif checknum<target:
            #print("less")
            pos+=step
        #checks to see if the number checked is less than the number checked and splices the list
        elif checknum>target:
            #print("interior")
            #print("more")
            lyst=lyst[(pos-(step)+1):pos]
            #print(lyst)
            for checknum in lyst:
                comp+=1
                #print("checknum"+str(checknum))
                if checknum==target:
                    return (True, comp)
            return(False,comp) 
    #if it never finds the number then creates a list of the last steps
    #print(pos)
    lyst=lyst[(pos-(step)+1):]
    #print("linear search")  
    #print(lyst)  
    for checknum in lyst:
        comp+=1
        
        #print("checknum"+str(checknum))
        if checknum==target:
            return (True, comp)
    return(False,comp)   
        

lyst = []      
for x in range(101):
    lyst.append(x)

for x in lyst:
    print("")
    print(x)
    print(jump_search(lyst, 87))