# from unittest import main
def binarySearch(mat,key):
    column = len(mat[0])
    low = 0;
    high = len(mat)*column - 1
    # print(low,high)
    while(low<=high):
        mid = (low+high)//2
        x,y = compute(mid,column)
        print(x,y)
        if mat[x][y]==key:
            return True;
        elif(mat[x][y]>key):
            high = mid-1
        else:
            low = mid+1;
    return False
def linear(x,y,column):
    res = x*column + y
    return res
def compute(n,column):
    y = n%column
    x = 0
    v = 0
    while (n>=column):
        n-=column
        x+=1
    return [x,y]
#       0  1  2  3  4  5  6  7  8
arr = [10,20,30,40,50,60,70,80,90]
mat = [
    [10,20,30],
    [40,50,60],
    [70,80,90],
]
# x,y = compute(7,len(mat[0]))
# print(x,y)
# print(mat[x][y])
# print(linear(1,2,len(mat[0])))
#-----------
print(binarySearch(mat,30))
