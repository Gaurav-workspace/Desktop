# matrix expoenentions

def multiply(m1,m2):
    
    return [
        [
            m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0],
            m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
        ],
        [
            m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0],
            m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
        ]
    ]
    # pass
def fib(n):
    if n==0:
        return [
            [1,0],
            [0,1]
        ]
    elif n==1:
        return [
            [1,1],
            [1,0]
        ]
    else:
        partition = fib(n//2)

        mul = multiply(partition,partition)
        if(n&1==1):
            return multiply(mul,fib(1))
        return mul;

m1 = [
    [1,1],
    [1,0]
]
m2 = [
    [1,1],
    [1,0]
]

print(fib(9))
"""
0 1 1 2 3 5 8 13 8
[2,1] [1,1]
[1,0] [1,0]
//---------
[2+1 , 2+0]
[1+0],[1+0]
//---------
[3,2]
[1,1]
"""