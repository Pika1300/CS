from random import randint
lyst=[]
for x in range(6):
    lyst.append(randint(1,1000))
#lyst=[2,1,3,4,5]
print(lyst)
def is_sorted(lyst):

    for x in range(len(lyst)-2):
        if (lyst[x+1] < lyst[x]):
            return False
    return True


def quicksort(lyst):
    rlyst=[]
    comparison=0
    totalswap=0
    checksper=0
    n1=0
    n2=1
    def sort(tlyst):
        if len(tlyst)==1:
            rlyst.append(tlyst[0])
        else:
            index1=0
            index2=len(tlyst)-1
            mid=int((index2-index1)/2)
            pivot=tlyst[mid]
            print("\nlist")
            print(tlyst)
            print("mid")
            print(mid)
            print("pivot")
            print(pivot)
            #print(tlyst[index1])
            #while index1<=index2 or index1==10:
            while tlyst[index1]<pivot:
                index1+=1
                #print()
                #print(tlyst[index1])
                #print(pivot)
            while tlyst[index2]>pivot:    
                index2-=1
            print(index1)
            print(index2)
            print(tlyst)
            temp=tlyst[index1]
            tlyst[index1]=tlyst[index2]
            tlyst[index2]=temp
            if index1==0 and index2==0:
                low=tlyst[0:1]
                high=tlyst[index2+1:len(lyst)]
            else:
                low=tlyst[0:index2]
                high=tlyst[index2:len(lyst)]
            
            
            print("\nindex1")
            print(index1)
            print("index2")
            print(index2)
            print("list")
            print(tlyst)
            print("low")
            print(low)
            print("high")
            print(high)
            print
            sort(low)
            sort(high)

    sort(lyst)
    print(rlyst,comparison,totalswap)
    return (rlyst,comparison,totalswap)


#print(lyst)
#lyst=[[1,2]]
#lyst=quicksort([7,4,6,18,8])
#print(is_sorted(lyst[0]))
lyst=[[True]]
while is_sorted(lyst[0])==True:
    lyst=[]
    print("___________________________________________________")
    for x in range(6):
        lyst.append(randint(1,1000))
    lyst=quicksort(lyst)
    print(is_sorted(lyst[0]))
