import time

def timecounter(func):
    start = time.time()
    def inner1(*args, **kwargs):
  
        # storing time before function execution
        begin = time.time()
          
        d=func(*args, **kwargs)
  
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return d
    return inner1
@timecounter
def iterative_fibo(n,st,nex):
    if(n==1):
        return st
    elif(n==2):
        return nex 
    else:
        for count in range(3,n+2):
            d=nex
            nex=st+nex
            st=d
        
        return st
@timecounter
def recursefibo(n,st,nex):
    def recursive_fibo(n,st,nex):
        if(n==1):
            return st
        if(n==2):
            return nex
        else:
            d=recursive_fibo(n-1,st,nex)+recursive_fibo(n-2,st,nex)
            #print(d)
            return d
    return recursive_fibo(n,st,nex)
@timecounter 
def tailoptfibo(n,st,nex):
    def go(n,st,nex):
        if(n==1):
            return st
        elif(n==2):
            return nex
        else:
            return go(n-1,nex,nex+st)
    return go(n,st,nex)
    
if(__name__=='__main__'):
    n=35
    
    f=iterative_fibo(n,0,1)
    d=recursefibo(n,0,1)
    g=tailoptfibo(n,0,1)
    print(f,d,g)
                
    