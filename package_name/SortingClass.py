import time
import math

class Sorting:
    
    #ats=array to sort
    #l=length
    
    
    def __init__(self,ats=[]):
        self.arr=ats
    
    
    
    def selectionSort(self):
        ats=self.arr
        l=len(self.arr)
        start = time.time()
        for i in range(l):
            min_idx = i
            for j in range(i+1,l):
                if ats[min_idx]>ats[j]:
                    min_idx=j
            
            ats[i],ats[min_idx]=ats[min_idx],ats[i]
            
        self.arr=ats
        t=time.time()-start
        self.disp(t,"Selection ")
                    
    def bubbleSort(self):
        ats=self.arr
        l=len(self.arr)
        start=time.time()  
        for i in range(l): 
            swapped = False
  
            # Last i elements are already 
            #  in place 
            for j in range(0, l-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
                if ats[j] > ats[j+1] : 
                    ats[j], ats[j+1] = ats[j+1], ats[j] 
                    swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
            if swapped == False: 
                break
        self.arr=ats
        t=time.time()-start
        self.disp(t,"Bubble ")
        
        
        
    def disp(self,t, algo):
        print(self.arr)
        print("Time taken by {}sort is {}s \n \n".format(algo,t/1000))    
        

    
    