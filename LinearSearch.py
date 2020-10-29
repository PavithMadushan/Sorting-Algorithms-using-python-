
def linearsearch(arr, x): 
   for i in range(len(arr)): 
      if arr[i] == x: # Compares array value to searched value
         return i # Returns index
   return -1

arr = [1,2,3,4,5,6,7,8,9,10] # Defines array

x = int(input("Enter a number between 1 and 10: ")) # Gets the user key value

print("element found at index "+str(linearsearch(arr,x))) # Displays where the value is found
