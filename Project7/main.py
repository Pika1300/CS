# import whatever you need here
import time
import sys
from hashmap import HashMap
from math import ceil
# Part 1 -- Write weight_on_cacheless() method
calls=0
def calc(r,c):
    global calls
    calls+=1
    if c<=0:
        l_weight=0
    else:
        l_weight=calc(r-1,c-1)
    if c>=r:
        r_weight=0
    else:
        r_weight=calc(r-1,c)

    return (200+(l_weight+r_weight)/2)

def weight_on_cacheless(r,c=None):
    if c==None:
        for x in range(r):
            for z in range(x+1):
                num=calc(x,z)
                print(num-200.0)
            print()
    else:
        num=calc(r,c)
        return(num-200.0)

# Part 3 -- Write weight_on_with_caching() method

def calchelp(cache,r,c):
    cache.fc()
    if c-1<0:
        
        lw=0
    else:
        cache.fc()
        cache.chit()
        lw=cache.get((r-1,c-1))
    if c>(r-1):
        
        rw=0
    else:
        cache.fc()
        cache.chit()
        rw=cache.get((r-1,c))
    
    return ((200+(lw+rw)/2))

def weight_on_cache(cache,r,c=None):
    
    cache.set((r,c),calchelp(cache,r,c))
    return cache.get((r,c))

def main():
    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    
    print("Cacheless:")
    start = time.perf_counter()
    i = 0
    num = 7
    
    f = open("with_caching.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    print("Number of function calls: " + str(calls))
    f.write("\nNumber of function calls: " + str(calls))
    f.close()
    
    # Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    h=HashMap()
    print()
    print("Cache:")
    start = time.perf_counter()
    row = 0
    height = 7
    
    f = open("cacheless.txt","w")
    while row < height:
        column = 0
        rp = ""
        while column <= row:
            rp += '{:.2f}'.format((weight_on_cache(h,row,column))-200) + " "
            column+=1
        print(rp)
        f.write(rp + '\n')
        row+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    print("Number of function calls: " + str(h.calls))
    f.write("\nNumber of function calls: " + str(h.calls))
    print("Number of cache hits: " + str(h.hits))
    f.write("\nNumber of cache hits: " + str(h.hits))
    f.close()


        

if __name__=="__main__":
    main()

