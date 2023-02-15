import random 
l=[0,1,2,3,4,5,6,7,8,9,40,90,50,30,92]
l.sort()
def binary_search(lyst,target):
    lyst.sort()
    last=len(lyst)
    first=0
    mid=(last-first)//2
    for x in range(8):

        #TestCode
        print("f"+str(first))
        print("m"+str(mid))
        print("l"+str(last))
        print("n"+str(lyst[mid]))
        print("")

        if lyst[mid] ==target:
            print("target:"+str(target) + " is found at index: "+str(mid))
            break
        elif first==mid:
            print("target:"+str(target) + " NOT found")
            break
        elif target>lyst[mid]:
            first=mid
            mid=((last-mid)//2)+mid
        else:
            last=mid
            mid=((last-first)//2)+first

xl=[0,1,2,3,4]            
#for z in range(random.randint(0,100)):
#    xl.append(random.randint(0,100))
print(xl)
for x in xl:
    binary_search(xl,0)