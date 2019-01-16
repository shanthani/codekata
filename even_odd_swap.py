m=input()
n=[x for x in m] 
print(n)
for i in range(0,len(n),2): 
    s="" n[i],n[i+1]=n[i+1],n[i] 
    s=s+n[i]+n[i+1] 
    print(s)
