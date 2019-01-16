def isprime(n):
    s=0
    for i in range(2,n):
        if n%i==0:
            s=s+1
    if s==0:
        return True
    else:
        return False
    
n,m=map(int,input().split())
c=0
for i in range(n,m+1):
    if isprime(i)==True:
        c=c+1
print(c)
    
