from random import seed, sample
from math import sqrt
def make_data(data_size):#DO NOT REMOVE OR MODIFY THIS FUNCTION
    '''A generator for producing data_size random values
    '''
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data

def linear_search(lyst, target):
    comparison=0
    for item in lyst:
        comparison+=1
        if item==target:
            return (True, comparison)
    return(False,comparison)


def binary_search(lyst, target):
    last=len(lyst)
    first=0
    mid=(last-first)//2
    comp=0
    while True:
        comp+=1
        """""
        #TestCode
        print("f"+str(first))
        print("m"+str(mid))
        print("l"+str(last))
        print("n"+str(lyst[mid]))
        """
        if lyst[mid] ==target:
            return (True, comp)
        elif first==mid:
            return (False, comp)   
        elif target>lyst[mid]:
            first=mid
            mid=((last-mid)//2)+mid
        else:
            last=mid
            mid=((last-first)//2)+first
            
def jump_search(lyst, target):
    comp=0
    step=sqrt(len(lyst))

def main():
    pass

if __name__ == "__main__":
    main()