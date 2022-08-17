def computeLcs(s1,s2,index1,index2):
    if index1==len(s1) or index2==len(s2):
        return []
    else:
        if s1[index1]==s2[index2]:
            nextArray = computeLcs(s1,s2,index1+1,index2+1)
            return [s1[index1],*nextArray]
        else:
            a = computeLcs(s1,s2,index1+1,index2)
            b = computeLcs(s1,s2,index1,index2+1)
            return a if len(a)>len(b) else b
    
    
s1 = "harrybhai"
s2 = "dynamicarray"
print(computeLcs(s1,s2,0,0))