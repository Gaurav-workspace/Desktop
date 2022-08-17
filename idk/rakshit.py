import random


def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    while low<high:
        if arr[low]<=pivot:
            i=i+1
            arr[low],arr[i]=arr[i],arr[low]
        low+=1
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def pivot_random(arr,low,high):
    r_pivot=random.randint(low,high)
    arr[high],arr[r_pivot]=arr[r_pivot],arr[high]
    return partition(arr,low,high)
def quicksort(arr,low,high):
    if (low<high):
        pivot_index=partition(arr,low,high)
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)
arr=[5,9,7,2,6,0,1]
n=len(arr)
print(arr)
quicksort(arr,0,n-1)
print("sorted array is:")
print(arr)