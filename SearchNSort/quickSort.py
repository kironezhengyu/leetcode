def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr,left,right):
    pivot = arr[(left+right)/2]
    #until we gone thorugh the whole array
    while left<=right:
        while arr[left]< pivot:
            left+=1
        while arr[right] > pivot:
            right-=1
        if left<=right:
            swap(arr,left,right)
            left+=1
            right-=1
    return left
def quicksort(arr,left,right):
    index = partition(arr,left,right)
    if left <index-1:
        quicksort(arr,left,index-1)
    if right > index:
        quicksort(arr,index,right)

arr = [1,231,23,2342,544,3253,41,232,3412,4324,12,412,34]
quicksort(arr,0,len(arr)-1)
print arr
