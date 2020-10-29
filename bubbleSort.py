def bubble_Sort(arr): 
    n = len(arr) 
    for i in range(n-1):   
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
                
arr = [30, 54, 65, 16, 43, 23, 9,43,34] 
bubble_Sort(arr) 
  
print ("Sorted arrayay using bubble sort:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  
