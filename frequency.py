def frequency(s):
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
        

s=input("Enter a string: ")
d=dict()
frequency(s)
print(d)
