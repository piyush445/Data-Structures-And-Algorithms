# If You Don't Know What A list is then: List is collection of data that can be of any Type.
# first We Create A fucntion
# Method 1 
def reverse(arr):
    length = len(arr)  # size of the list 
    for i in range(length//2):  # It iterates til mid of the list and swaps elements
        arr[i] , arr[(length-i)-1] = arr[(length-i)-1] , arr[i]
n = input("Enter Numbers given by space: ")  # here i Specify to Give Space otherwise 12345 will be considerd as one string not numbers and then cannot be splitted 
n = n.split() # It splits the string. Defalut parameter is space (" ")
arr = [int(e) for e in n] # It converts string element to int and append into arr
reverse(arr) 
print(arr)

#Time Complexity = O(n) + O(n/2) = O(n)
#Space Complexity = O(n)

# Method 2

n = list(map(int,input("Enter number by space").split())) # It takes space seperated integer values and map to list
n = n[::-1]    # It slices the list in reverse order
print(n)
