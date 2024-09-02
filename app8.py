# my_numbers = [4,7,8,5,15,6,10,]

# fav_number = 5

# def linear_search(collection,searched):
#     for i in range(len(collection)):
#         if collection[i] == searched:
#             return i
#     return -1

# linear_search(my_numbers,fav_number)

# fav_index = linear_search(my_numbers,fav_number)

# print(fav_index)
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if (swapped == False):
#             break
#         if __name__ == "__main__":
#             arr = [64, 34, 25, 12, 22, 11, 90]

#     bubbleSort(arr)

#     print("Sorted array:")
#     for i in range(len(arr)):
#         print("%d" % arr[i], end=" ")

# def insertionSort(arr):
#     n = len(arr)  
      
#     if n <= 1:
#         return 
 
#     for i in range(1, n):  
#         key = arr[i]  
#         j = i-1
#         while j >= 0 and key < arr[j]:  
#             arr[j+1] = arr[j] 
#             j -= 1
#         arr[j+1] = key  
  
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print(arr)

# list = [3, 7, 4, 2, 6, 5]

# def oz_listim(list):
#     n = len(list)
#     ayrilt_index = n // 2

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
  
def mergeSort(arr, l, r):
    if l < r:
 
        
        
        m = l+(r-l)//2
 
     
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is: ")
for i in range(n):
    print("%d" % arr[i],end=" ")

