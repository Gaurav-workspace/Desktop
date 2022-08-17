def encodeString(str):
    res=""
    cap = [chr(i) for i in range(65,91)]
    small = [chr(i) for i in range(97,123)]
    for i in str:
        value = ord(i)
        if value>=65 and value<=90:
            value = value-65
            value+=13
            value%=len(cap)
            res+=cap[value];
        elif value>=97 and value<=122:
            value = value-97
            value+=13
            value%=len(small)
            res+=small[value];
        else:
            res+=i
    return res
