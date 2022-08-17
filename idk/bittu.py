def printResult(arr, n):

    n_sum = 0
    s = set()
    chk=0
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            chk=1
            break
        s.add(n_sum)
 
    if chk:
        print("true")
    else:
        print("false")
print([])