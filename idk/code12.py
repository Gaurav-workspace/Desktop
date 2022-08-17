def ReplaceDiagonal(mat,m):
    if m==1 or m==0:
        return mat
    for i in range(m):
        res = 0
        if i==0:
            res+=mat[0][1]
            res+=mat[1][0]
            res+=mat[1][1]
            mat[i][i] = res
        elif i==m-1:
            res+=mat[m-2][m-2]
            res+=mat[m-1][m-2]
            res+=mat[m-2][m-1]
            mat[i][i] = res
        else:
            res+=mat[i-1][i+1]
            res+=mat[i-1][i]
            res+=mat[i-1][i-1]

            res+=mat[i][i+1]
            res+=mat[i][i-1]

            res+=mat[i+1][i-1]
            res+=mat[i+1][i]
            res+=mat[i+1][i+1]
            mat[i][i] = res
    return mat



print(ReplaceDiagonal(
    [
        [12,20],
        [10,22]
    ]
,2))
            