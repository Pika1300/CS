from random import randint
lyst=[]
for x in range(50):
    lyst.append(randint(1,1000))
#lyst=[2,1,3,4,5]
print(lyst)
def is_sorted(lyst):
    if type(lyst)!= list:
        raise Exception("Not a list")
    else:
        for x in range(len(lyst)-2):
            if (lyst[x+1] < lyst[x]):
                return False
        return True


def insertion_sort(lyst):
    comparison=0
    totalswap=0
    checksper=0
    n1=0
    n2=1
    while(checksper<(len(lyst)-1)):
        checksper+=1
        comparison+=1
        if lyst[n2]<lyst[n1]:
            lyst[n1],lyst[n2]=lyst[n2],lyst[n1]
            checksper=0
            totalswap+=1
            n1=0
            n2=1
        else:
            n1+=1
            n2+=1

    print(lyst,comparison,totalswap)
    return (lyst,comparison,totalswap)


print(lyst)
lyst=insertion_sort(lyst)
print(lyst)
print(is_sorted(lyst[0]))
